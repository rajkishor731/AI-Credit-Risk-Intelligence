def analyze_news_risk(news_list):

    if not news_list:
        return "No significant news risks detected."

    risk_keywords = [
        "fraud",
        "lawsuit",
        "bankruptcy",
        "investigation",
        "debt",
        "corruption",
        "scandal",
        "default",
        "penalty"
    ]

    risks_found = []

    for news in news_list:
        for word in risk_keywords:
            if word.lower() in news.lower():
                risks_found.append(news)
                break

    if risks_found:
        summary = "Potential credit risks detected from recent news:\n\n"
        for r in risks_found:
            summary += f"- {r}\n"
        return summary

    return "Recent news does not indicate major financial or legal risks."