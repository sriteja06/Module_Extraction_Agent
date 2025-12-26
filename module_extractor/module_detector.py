import re
import openai
import os
from dotenv import load_dotenv
from .parser import clean_text

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def ai_summary(text_chunk):
    prompt = f"""
    Extract modules and submodules from this documentation text.
    Output JSON example:
    {{
      "module": "...",
      "description": "...",
      "submodules": {{
        "name": "description"
      }}
    }}
    TEXT: {text_chunk}
    """
    res = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )
    return res.choices[0].message.content

def extract_modules(text):
    text = clean_text(text)
    chunks = re.split(r"\. |\n{2,}", text)
    results = []

    for chunk in chunks:
        words = chunk.split()
        if len(words) < 10:   # <-- LOOSENED requirement
            continue
        try:
            js = ai_summary(chunk)
            results.append(js)
        except Exception as e:
            print("[AI Extraction Error]", e)
            continue

    return {"modules": results}
