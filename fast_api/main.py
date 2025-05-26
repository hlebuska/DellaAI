from fastapi import FastAPI, Request
from pydantic import BaseModel
from db import database, messages
from datetime import datetime
import os
import json

class MessageIn(BaseModel):
    user_id: int
    text: str

app = FastAPI()

@app.get("/all-messages")
async def get_all_messages():
    query = messages.select()
    result = await database.fetch_all(query)
    return result

@app.post("/process-message")
async def process_message(payload: MessageIn):
    gpt_response = 'response will be here!'

    # Save to SQLite
    query = messages.insert().values(
        user_id=payload.user_id,
        text=payload.text,
        gpt_response=json.dumps(gpt_response),
        timestamp=datetime.utcnow()
    )
    await database.execute(query)

    return {"reply": f"Action: {'action will be here!'}"}

# entry for tg bot to drop raw text -> process it to chatgpt -> see if its a command 