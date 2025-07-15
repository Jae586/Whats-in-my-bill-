# gpt/summarize.py

import openai
import os
from dotenv import load_dotenv
from gpt.prompts import SUMMARY_PROMPT

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_bill(text):
    print("🤖 Summarizing bill...")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a policy expert summarizing U.S. legislation."},
            {"role": "user", "content": SUMMARY_PROMPT.format(text=text)}
        ]
    )
    return response.choices[0].message.content
