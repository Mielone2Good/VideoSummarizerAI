from Backend.ai_core import AiCore

class YoutubeSummarizerAI():
    def __init__(self):
        self.ai_core = AiCore()
        self.ai_core.load_model()
        self.max_model_input = self.ai_core.max_model_input

    def summarize_text(self, text: str) -> str:
        """
        Summarize long text/document with local LLM, 
        
        Algorithm will split text into chunks and generate sub-summary for each chunk
        Splitting chunks and generating sub-summary until text matches maximum model input length
        then connect all chunks to generate final summary.
        """
        text_to_summarize = text
        finished = False
        new_max_chunk_length = self.max_model_input - 80

        while not finished:
            if self.max_model_input > self.ai_core.get_tokens_length(text = text_to_summarize):
                try:
                    result = self.ai_core.summarize(text = text_to_summarize, max_output_length = 350)
                    return {'summary':result, 'status':'ok'}
                except Exception as e:
                    return {'error':e, 'status':'error'}
                finally:
                    finished = True
                
            else:
                chunks = self.ai_core.split_into_chunks(text = text_to_summarize, max_chunk_length = new_max_chunk_length)
                summarized_chunks = []
                max_output = new_max_chunk_length // 3
                for chunk in chunks:
                    chunk_result = self.ai_core.summarize(text = chunk, max_output_length = max_output)
                    summarized_chunks.append(chunk_result)

                text_to_summarize = " ".join(summarized_chunks)
                new_max_chunk_length -= 80

            


            

