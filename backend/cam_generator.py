from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def generate_cam(company, financials, ratios, risks, score, decision):

    file_name = f"{company}_CAM_Report.pdf"

    c = canvas.Canvas(file_name, pagesize=letter)

    y = 750

    c.setFont("Helvetica-Bold", 18)
    c.drawString(200, y, "Credit Appraisal Memo")
    y -= 40

    c.setFont("Helvetica", 12)

    c.drawString(50, y, f"Company: {company}")
    y -= 30

    c.drawString(50, y, "Financial Data:")
    y -= 20

    for key, value in financials.items():
        c.drawString(70, y, f"{key}: {value}")
        y -= 20

    y -= 10
    c.drawString(50, y, "Financial Ratios:")
    y -= 20

    for key, value in ratios.items():
        c.drawString(70, y, f"{key}: {value}")
        y -= 20

    y -= 10
    c.drawString(50, y, "Risk Signals:")
    y -= 20

    if risks:
        for r in risks:
            c.drawString(70, y, r[:90])
            y -= 20
    else:
        c.drawString(70, y, "No major risks detected")
        y -= 20

    y -= 20

    c.drawString(50, y, f"Credit Score: {score}")
    y -= 30

    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, f"Loan Decision: {decision}")

    c.save()

    print(f"\nCAM Report generated: {file_name}")