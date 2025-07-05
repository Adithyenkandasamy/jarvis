from llm.ollama_client import ollama_response

def get_llm_reply(prompt: str) -> str:
    response = ollama_response(prompt)
    return response
