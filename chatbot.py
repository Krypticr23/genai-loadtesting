from fastapi import FastAPI, Request
import google.generativeai as genai
import os

app = FastAPI()

GEMINI_API_KEY = "AIzaSyDd9ygBYnOtmDFx16OORdIxGGxBw44ni60"
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("models/gemini-1.5-flash")

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    article = data.get("article", "")
    prompt = f"Summarize this article:\n{article}"

    try:
        response = model.generate_content(prompt)
        return {"summary": response.text}
    except Exception as e:
        return {"error": str(e)}
