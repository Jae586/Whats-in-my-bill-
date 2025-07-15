# gpt/prompts.py

SUMMARY_PROMPT = """
Summarize the following U.S. Senate bill in this format:

1. TL;DR (4 sentences)
2. What the bill does (3–5 bullets)
3. Who is affected
4. Political support or opposition
5. Legal/financial implications
6. Suggest 1–2 ideas for data visuals that could help readers understand this bill.

Bill Text:
{text}
"""
