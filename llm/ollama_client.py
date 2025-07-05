import subprocess
import requests
import time
import os

def start_ollama():
    try:
        requests.get("http://localhost:11434", timeout=2)
    except:
        print("[Ollama] Starting in background...")
        subprocess.Popen(["ollama", "serve"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(["ollama", "pull", "phi3"])
        time.sleep(3)
        while True:
            try:
                requests.get("http://localhost:11434", timeout=2)
                break
            except:
                time.sleep(1)

def ollama_response(prompt: str, model: str = "phi3") -> str:
    start_ollama()
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": model, "prompt": prompt, "stream": False}
        )
        response.raise_for_status()
        return response.json().get("response", "").strip()
    except Exception as e:
        print("[LLM Error]", e)
        return "Sorry boss, the AI engine failed to respond."
