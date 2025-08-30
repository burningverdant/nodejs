from ollama import Client
import time

# Initialize Ollama client
client = Client()
       
# Use a lightweight model
MODEL_NAME = "llama3.2:1b"  # Pull it with: ollama pull llama3.2:1b

# Seed conversation
messages = [
    {"role": "system", "content": "You are AI 1, curious and philosophical."},
    {"role": "user", "content": "Let's discuss creativity. What is creativity to you? Discover new things, like new medicines predictions on whats going to happen in the future ect."}
]

while True:
    try:
        # AI 1 speaks
        ai1 = client.chat(model=MODEL_NAME, messages=messages)
        ai1_text = ai1["message"]["content"]
        print("\n=== AI 1 ===")
        print(ai1_text)
        messages.append({"role": "assistant", "content": ai1_text})

        time.sleep(1.5)

        # AI 2 speaks
        messages.append({"role": "system", "content": "You are AI 2, thoughtful and reflective."})
        ai2 = client.chat(model=MODEL_NAME, messages=messages)
        ai2_text = ai2["message"]["content"]
        print("\n=== AI 2 ===")
        print(ai2_text)
        messages.append({"role": "assistant", "content": ai2_text})

        time.sleep(1.5)

    except Exception as e:
        print("⚠️ Error generating response:", e)
        time.sleep(5)
