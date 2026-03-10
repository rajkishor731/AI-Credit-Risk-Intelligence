from extractor import extract_text
from financial_analysis import extract_financial_data, calculate_ratios
from scoring import credit_score, loan_decision
from research_agent import search_company_news, detect_risk_signals
from cam_generator import generate_cam


# -------- Company Name --------

company = "Adani"


# -------- Financial Analysis --------

text = extract_text("data/company_report.pdf")

financials = extract_financial_data(text)

ratios = calculate_ratios(financials)


# -------- News Research --------

news = search_company_news(company)

risks = detect_risk_signals(news)


# -------- Credit Scoring --------

score = credit_score(ratios, risks)

decision = loan_decision(score)


# -------- Output --------

print("\n--------- Financial Analysis ---------")
print("Financial Data:", financials)
print("Financial Ratios:", ratios)

print("\n--------- News Analysis ---------")
print("Recent News:", news)
print("Risk Signals:", risks)

print("\n--------- Credit Decision ---------")
print("Credit Score:", score)
print("Loan Decision:", decision)


# -------- CAM Report Generation --------

generate_cam(company, financials, ratios, risks, score, decision)