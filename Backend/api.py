from contextlib import asynccontextmanager
from fastapi import FastAPI
from typing import Union
from Backend.ai_algorithm import YoutubeSummarizerAI
from Backend.get_transcript import get_transcript

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Server Start ------------------------")
    app.state.service = YoutubeSummarizerAI()
    print("AI Core loaded ------------------------")

    yield

    print("Sever shutdown... -------------------------------")

app = FastAPI(lifespan = lifespan)

@app.get('/')
def root():
    return {'Hello':'World'}

@app.get("/summarize-video")
async def process_video(url: Union[str, None] = None, length: Union[int, None] = 500):
    """
    Endpoint
    Summarize youtube video using local LLM
    Params: video url
    """
    if not url:
        return {'error':'please provide youtube video url'}

    ai = app.state.service
    transcript = get_transcript(url)

    if transcript['status'] != 'ok':
        return {
            'error':transcript['error'], 
            'received_url': url, 
            'status':transcript['status']
        }

    response = ai.summarize_text(text = transcript['transcript'], output_length = length)

    if response['status'] == 'ok':
        return {
            'summary':response['summary'], 
            'received_url': url, 
            'status':response['status']
        }
    
    elif response['status'] == 'error':
        return {
            'error':response['error'], 
            'received_url': url, 
            'status':response['status']
        }