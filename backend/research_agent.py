import requests

API_KEY = "8356b3142b804cdba34e74b639ba3acd"

def search_company_news(company_name):

    url = f"https://newsapi.org/v2/everything?q={company_name} AND (fraud OR lawsuit OR investigation OR debt OR default)&language=en&sortBy=publishedAt&apiKey={API_KEY}"
    
    response = requests.get(url)

    print("Status:", response.status_code)

    data = response.json()

    if "articles" not in data:
        print(data)
        return []

    headlines = []

    for article in data["articles"][:5]:
        headlines.append(article["title"])

    return headlines


def detect_risk_signals(headlines):

    risk_words = [
        "fraud",
        "scam",
        "investigation",
        "bankruptcy",
        "lawsuit",
        "default",
        "insolvency"
    ]

    risks = []

    for headline in headlines:
        for word in risk_words:
            if word.lower() in headline.lower():
                risks.append(headline)

    return risks