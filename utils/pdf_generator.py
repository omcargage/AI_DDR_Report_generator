from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
import os

def clean_text(text):
    import re

    # remove markdown symbols
    text = re.sub(r"#", "", text)
    text = re.sub(r"\*", "", text)
    text = re.sub(r"\!", "", text)

    return text

def generate_pdf(report_text, image_paths, output_path="report.pdf"):

    doc = SimpleDocTemplate(output_path)
    styles = getSampleStyleSheet()

    elements = []

    # 🔹 Add text (split into lines)
    for line in report_text.split("\n"):
        clean_line = clean_text(line)
        elements.append(Paragraph(line, styles["Normal"]))
        elements.append(Spacer(1, 10))

    # 🔹 Add images
    for img_path in image_paths:
        if os.path.exists(img_path):
            elements.append(Image(img_path, width=300, height=200))
            elements.append(Spacer(1, 10))

    doc.build(elements)

    return output_path