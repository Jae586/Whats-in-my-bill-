# gpt/generate_figures.py

import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_figure_data(summary_text):
    print("📊 Generating figure ideas and mock data...")
    
    prompt = f"""
From the following summary of a U.S. Senate bill, suggest one figure idea and generate simple mock data in JSON format.

Example output:
---
Chart Title: Projected Spending (2025–2030)
Data:
{{
  "years": [2025, 2026, 2027, 2028],
  "spending": [100, 120, 135, 150]
}}

Summary:
{summary_text}
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You generate figure data for newsletter charts."},
            {"role": "user", "content": prompt}
        ]
    )

    content = response.choices[0].message.content
    return extract_figure_idea_and_data(content)

def extract_figure_idea_and_data(content):
    import re, json
    title_match = re.search(r"Chart Title:\s*(.+)", content)
    data_match = re.search(r"Data:\s*({.*})", content, re.DOTALL)

    title = title_match.group(1).strip() if title_match else "Untitled Chart"
    data_json = data_match.group(1).strip() if data_match else "{}"
    try:
        data = json.loads(data_json)
    except json.JSONDecodeError:
        data = {}

    return title, data
