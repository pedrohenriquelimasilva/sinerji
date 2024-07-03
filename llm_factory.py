from llm_client import ChatGPTClient, TransformersModel

class LLMFactory:
    @staticmethod
    def create_client(model_name):
        if model_name == "chatgpt":
            return ChatGPTClient()
        elif model_name == "bert-base-uncased":
            return TransformersModel(model_name)
        else:
            raise ValueError(f"Unknown model: {model_name}")
