# run_pipeline.py

from pipeline.fetch_bills import get_recent_senate_bills
from gpt.summarize import summarize_bill
from gpt.generate_figures import get_figure_data
from charts.chart_generator import generate_charts
from newsletter.build_draft import build_newsletter_draft
import os
from datetime import datetime

def main():
    print("🔍 Fetching recent Senate bills...")
    bills = get_recent_senate_bills(limit=1)  # you can change to >1 later

    for bill in bills:
        print(f"📄 Processing bill: {bill['title']} ({bill['bill_id']})")

        # Summarize
        summary = summarize_bill(bill["text"])

        # Generate figure data
        figure_ideas, figure_data = get_figure_data(summary)

        # Generate charts
        chart_paths = generate_charts(figure_data)

        # Build final draft
        today = datetime.now().strftime("%Y-%m-%d")
        filename = f"output/newsletter_{today}.md"
        build_newsletter_draft(bill, summary, chart_paths, filename)

        print(f"✅ Draft saved to {filename}\n")

if __name__ == "__main__":
    main()
