import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

from backend.extractor import extract_text
from backend.financial_analysis import extract_financial_data, calculate_ratios
from backend.scoring import credit_score, loan_decision
from backend.research_agent import search_company_news, detect_risk_signals
from backend.ai_risk_analyzer import analyze_news_risk
from backend.cam_generator import generate_cam


st.set_page_config(page_title="AI Credit Risk Intelligence Platform", layout="wide")

st.title("AI Credit Risk Intelligence Platform")
st.markdown("Analyze company financial health and credit risk using AI.")


# ---------- SIDEBAR ----------

st.sidebar.title("Control Panel")

company = st.sidebar.text_input("Enter Company Name")

uploaded_file = st.sidebar.file_uploader("Upload Financial Report (PDF)", type=["pdf"])

analyze_button = st.sidebar.button("Run Credit Analysis")


# ---------- MAIN PROCESS ----------

if analyze_button:

    if uploaded_file is not None and company != "":

        with open("temp_report.pdf", "wb") as f:
            f.write(uploaded_file.read())

        text = extract_text("temp_report.pdf")

        financials = extract_financial_data(text)

        ratios = calculate_ratios(financials)

        news = search_company_news(company)

        risks = detect_risk_signals(news)

        ai_risk_summary = analyze_news_risk(news)

        score = credit_score(ratios, risks)

        decision = loan_decision(score)

        if score >= 80:
            risk_level = "Low Risk"
        elif score >= 65:
            risk_level = "Moderate Risk"
        else:
            risk_level = "High Risk"

        generate_cam(company, financials, ratios, risks, score, decision)

        tab1, tab2, tab3, tab4 = st.tabs([
            "Overview",
            "Financial Analysis",
            "News Intelligence",
            "Credit Decision"
        ])

        # ---------- OVERVIEW ----------

        with tab1:

            st.subheader("Credit Risk Overview")

            col1, col2, col3, col4 = st.columns(4)

            col1.metric("Revenue", f"₹{financials.get('revenue',0):,}")
            col2.metric("Profit", f"₹{financials.get('profit',0):,}")
            col3.metric("Debt", f"₹{financials.get('debt',0):,}")
            col4.metric("Credit Score", score)


        # ---------- FINANCIAL ANALYSIS ----------

        with tab2:

            st.subheader("Financial Data")

            col1, col2, col3 = st.columns(3)

            col1.metric("Revenue", f"₹{financials.get('revenue',0):,}")
            col2.metric("Profit", f"₹{financials.get('profit',0):,}")
            col3.metric("Debt", f"₹{financials.get('debt',0):,}")

            st.divider()

            st.subheader("Financial Ratios")

            col1, col2 = st.columns(2)

            col1.metric(
                "Profit Margin",
                f"{ratios.get('profit_margin',0)*100:.2f}%"
            )

            col2.metric(
                "Debt Ratio",
                f"{ratios.get('debt_ratio',0)*100:.2f}%"
            )

            ratio_names = list(ratios.keys())
            ratio_values = list(ratios.values())

            fig = px.bar(
                x=ratio_names,
                y=ratio_values,
                title="Financial Ratio Analysis",
                labels={"x":"Ratio","y":"Value"}
            )

            st.plotly_chart(fig)


        # ---------- NEWS ----------

        with tab3:

            st.subheader("Recent News")

            if news:
                for n in news:
                    st.info(n)

            else:
                st.write("No recent news found.")


            st.subheader("Risk Signals")

            if risks:
                for r in risks:
                    st.warning(r)

            else:
                st.success("No major risk signals detected")


            st.subheader("AI Risk Analysis")

            st.write(ai_risk_summary)


        # ---------- CREDIT DECISION ----------

        with tab4:

            st.subheader("Credit Score")

            fig_gauge = go.Figure(go.Indicator(
                mode="gauge+number",
                value=score,
                title={'text': "Credit Score"},
                gauge={
                    'axis': {'range': [0, 100]},
                    'bar': {'color': "green"},
                    'steps': [
                        {'range': [0, 50], 'color': "#ffcccc"},
                        {'range': [50, 65], 'color': "#ffe6cc"},
                        {'range': [65, 80], 'color': "#ffffcc"},
                        {'range': [80, 100], 'color': "#ccffcc"}
                    ],
                }
            ))

            st.plotly_chart(fig_gauge)

            st.subheader("Risk Classification")

            st.write(risk_level)

            st.subheader("Loan Decision")

            if decision == "APPROVE":
                st.success(decision)

            elif decision == "APPROVE WITH CONDITIONS":
                st.warning(decision)

            else:
                st.error(decision)

            st.subheader("Download Credit Appraisal Memo")

            with open(f"{company}_CAM_Report.pdf","rb") as file:

                st.download_button(
                    label="Download CAM Report",
                    data=file,
                    file_name=f"{company}_CAM_Report.pdf"
                )

    else:

        st.warning("Please enter company name and upload a PDF.")