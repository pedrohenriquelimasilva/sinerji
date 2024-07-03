from transformers import BertLMHeadModel, BertTokenizer, pipeline
import openai
import os
from dotenv import load_dotenv
from abc import ABC, abstractmethod

class LLMClient(ABC):
    @abstractmethod
    def get_completion(self, messages = str):
        pass

load_dotenv()
class ChatGPTClient(LLMClient):
    def __init__(self):
        openai.api_key = os.environ.get("OPENAI_API_KEY")
        self.client = openai.OpenAI(api_key=openai.api_key)

    def get_completion(self, message):
        response = self.client.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message}
            ],
            temperature=1,
            max_tokens=200
        )
        return response.choices[0].message.content

# uso do Bert - incompleto
class TransformersModel(LLMClient):
    def __init__(self, model_name):
        self.tokenizer = BertTokenizer.from_pretrained(model_name)
        self.model = BertLMHeadModel.from_pretrained(model_name, is_decoder=True)

    def get_completion(self, prompt: str) -> str:
        inputs = self.tokenizer(prompt, return_tensors="pt")
        input_ids = inputs["input_ids"]

        num_beams = 4  
        max_length = 150  
        
        # Gerar saída do modelo
        outputs = self.model.generate(
            input_ids,
            max_length=max_length,
            num_beams=num_beams,
            early_stopping=True 
        )
        
        # Decodificar a saída
        decoded_output = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        return decoded_output
