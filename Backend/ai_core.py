import torch
from transformers import BartForConditionalGeneration, BartTokenizer
from Backend.get_transcript import get_transcript

class AiCore():
    def __init__(self, model_name: str = 'facebook/bart-large-cnn'):
        self.model_name = model_name
        self.max_model_input = 1024 #1024
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    
    def load_model(self):
        self.tokenizer = BartTokenizer.from_pretrained(self.model_name)
        self.model = BartForConditionalGeneration.from_pretrained(self.model_name).to(self.device)

    def split_into_chunks(self, text: str, max_chunk_length: int = 900, chunk_overloop: int = 40) -> list:
        """
        Splits the input text into chunks of a specified maximum length, allowing for some overlap.
        """
        tokens = self.tokenizer.tokenize(text)
        real_chunk_length = max_chunk_length - chunk_overloop

        chunks = []
        for i in range(0, len(tokens), real_chunk_length):
            chunks.append(tokens[i:i + max_chunk_length])

        text_chunks = []
        for chunk in chunks:
            ids = self.tokenizer.convert_tokens_to_ids(chunk)
            text_chunks.append(self.tokenizer.decode(ids, skip_special_tokens=True))
            
        return text_chunks

    def summarize(self, text: str, max_output_length: int = 300) -> str:
        """
        Use AI to summarize text
        """
        if not(self.model): self.load_model()
        accepted_input_length = self.max_model_input - 200
        
        encoded_input = self.tokenizer.encode("summarize: " + text, return_tensors = 'pt', max_length = accepted_input_length, truncation = True).to(self.device)
        generated_output = self.model.generate(encoded_input, 
            max_length = max_output_length, 
            min_length = max_output_length // 3, 
            early_stopping = True, 
            length_penalty = 9.0, 
            num_beams = 4)
        decoded_output = self.tokenizer.decode(generated_output[0], skip_special_tokens = True)

        return decoded_output
    
    def get_tokens_length(self, text: str) -> int:
        """
        Check tokens length from a text.
        """
        if not(self.tokenizer): self.load_model()
        tokens_length = len(self.tokenizer.tokenize(text))
        return tokens_length
