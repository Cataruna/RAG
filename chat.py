import subprocess
import requests

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "qwen-local"

def ask_qwen(query):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "messages": [
                {"role": "user", "content": query},
            ],
            "stream": False,
            "think": False,
            "keep_alive": 0,
        },
    )

    response.raise_for_status()
    return response.json()["message"]["content"]



def speak(text):
    subprocess.run(
        ["uv", "run", "python", "speak.py", text],
        cwd=r"D:\Proiecte\RAG\index-tts",
        check=True,
    )


query = input("You: ")
answer = ask_qwen(query)
print(f"\nQwen: {answer}\n")

speak(answer)