import gradio as gr
import requests
import time
import asyncio

summary_length_options = {
    "very short": 200,
    "short": 300,
    "normal": 500,
    "long": 700,
    "very long": 800
}

async def summarize_youtube_video(youtube_url: str, length_choice: str, status_box):
    if not youtube_url.strip():
        return "","Incorrect Youtube URL"

    try:
        api_payload = {
            "url": youtube_url,
            "length": summary_length_options[length_choice]
        }

        response = requests.get("http://localhost:8000/summarize-video", params=api_payload)
        response.raise_for_status()
        data = response.json()

        if data.get('status','error') != 'ok':
            return "", f"❌ Error: {data.get('error','Error')}"

        return data.get('summary','AI Error'), "✅ Finished"
    
    except requests.exceptions.RequestException as e:
        return "", f"❌ API Error: {e}"
    except Exception as e:
        return "", f"❌ Unknow error: {e}"


with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# YouTube Video Summarizer - LLM", elem_classes="title")
    gr.Markdown("Please paste youtube video url, you can also select summary length")
    with gr.Row():
        youtube_url = gr.Textbox(label="Youtube Video URL", placeholder="https://www.youtube.com/watch?v=...")
        length_choice = gr.Dropdown(
            choices=list(summary_length_options.keys()),
            value="normal",
            label="Summary Length"
        )
    submit_button = gr.Button("✅ Generate Summary")

    with gr.Group():
        status_box = gr.Textbox(value="", label="Status", interactive=False)
        summary_output = gr.Textbox(label="AI Summary", lines=15, interactive=False, scale=2)

    submit_button.click(
        fn=summarize_youtube_video,
        inputs=[youtube_url, length_choice, status_box],
        outputs=[summary_output, status_box]
    )


demo.launch()
