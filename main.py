# main.py
import subprocess
import time
import uvicorn

def start_ollama():
    print("Starting Ollama server...")
    subprocess.Popen(["ollama", "serve"])
    time.sleep(5)

if __name__ == "__main__":
    start_ollama()
    print("Starting API server...")
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
