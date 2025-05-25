# pdf_report.py
from fpdf import FPDF
import tempfile
import os


def generate_pdf_report(results, explanations):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Medical Report Summary", ln=True, align='C')
    pdf.ln(10)

    for r in results:
        pdf.set_font("Arial", size=10)
        pdf.cell(0, 10, txt=f"{r['test']}: {r['value']} {r['unit']} (Normal: {r['ref_range']}) - {r['status']}",
                 ln=True)

    pdf.ln(10)
    pdf.set_font("Arial", 'B', size=12)
    pdf.cell(0, 10, txt="Explanations", ln=True)
    pdf.set_font("Arial", size=10)

    for e in explanations:
        pdf.multi_cell(0, 10, txt=f"{e['test']}:\n{e['explanation']}")
        pdf.ln(5)

    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    pdf.output(temp_file.name)
    return temp_file.name
