import os
import openai
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

# Replace "your_openai_api_key" with your actual OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.post("/chat/")
async def chat(message: str = Form(...)):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message},
        ]
    )
    return {"response": response.choices[0].message['content']}
