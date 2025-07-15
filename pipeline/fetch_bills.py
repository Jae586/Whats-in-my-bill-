# pipeline/fetch_bills.py

import requests
import os
from dotenv import load_dotenv

load_dotenv()

CONGRESS_API_KEY = os.getenv("CONGRESS_API_KEY")

def get_recent_senate_bills(limit=1):
    url = f"https://api.congress.gov/v3/bill"
    params = {
        "api_key": CONGRESS_API_KEY,
        "congress": "118",
        "billType": "s",
        "pageSize": limit,
        "format": "json"
    }
    resp = requests.get(url, params=params)
    bills = resp.json().get("bills", [])

    results = []
    for bill in bills:
        bill_id = bill.get("number")
        title = bill.get("title") or "No title available"
        text_url = bill.get("latestAction", {}).get("textLink", "")

        # Fallback: simulate full text retrieval
        full_text = f"[Full text of {title} not fetched yet — simulated for dev]"

        results.append({
            "bill_id": bill_id,
            "title": title,
            "text": full_text
        })

    return results
