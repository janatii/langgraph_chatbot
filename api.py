from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from main import graph
import uvicorn
import json


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

class ChatRequest(BaseModel):
    message: str
    history: list = []

@app.post("/chat")
async def chat_endpoint(req: ChatRequest):
    state = {"messages": req.history + [{"role": "user", "content": req.message}], "message_type": None}
    result = graph.invoke(state)
    messages = []
    for msg in result.get("messages", []):
        if hasattr(msg, 'type') and hasattr(msg, 'content'):
            if msg.type == "human":
                role = "user"
            elif msg.type == "ai":
                role = "assistant"
            else:
                role = msg.type
            content = msg.content
        elif hasattr(msg, 'role') and hasattr(msg, 'content'):
            role = getattr(msg, 'role', None)
            content = getattr(msg, 'content', None)
        elif isinstance(msg, dict):
            role = msg.get('role')
            content = msg.get('content')
        else:
            try:
                msg_json = json.loads(msg.json())
                role = msg_json.get('role')
                content = msg_json.get('content')
            except Exception:
                continue
        messages.append({"role": role, "content": content})
    reply = ""
    for msg in reversed(messages):
        if msg["role"] == "assistant":
            reply = msg["content"]
            break
    return {"reply": reply, "history": messages}

@app.get("/", response_class=HTMLResponse)
def index():
    with open("static/index.html") as f:
        return HTMLResponse(f.read())

if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)
