# server.py
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from vexyapi import VexyAPI

app = FastAPI()
vexy = VexyAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_message = data.get("message", "")
    messages = data.get("messages", [])

    # Append user message to conversation
    messages.append({"role": "user", "content": user_message})

    # Get AI response
    ai_response = vexy.generate_response(messages)
    messages.append({"role": "assistant", "content": ai_response})

    return {"response": ai_response, "messages": messages}
