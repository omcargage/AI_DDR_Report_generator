# 🏗️ AI DDR Report Generator

## 📌 Overview

This project is an AI-powered system that converts **inspection reports and thermal reports** into a structured **Detailed Diagnostic Report (DDR)**.

The system processes unstructured PDF inputs and generates a clear, client-friendly report with insights, severity assessment, and recommendations.

---

## 🚀 Features

* 📄 Extracts text from inspection & thermal reports
* 🧠 Rule-based AI pipeline for issue detection
* 🏢 Area-wise grouping of observations
* 🔁 Deduplication of repeated issues
* 🔍 Root cause analysis
* ⚠️ Severity assessment with reasoning
* 🧾 Structured DDR report generation
* 🖼️ Image extraction from reports
* 📥 Downloadable PDF report
* 🌐 Simple Streamlit UI

---

## 🧠 System Architecture

```
PDF → Text Extraction → Issue Detection → Area Mapping → Deduplication  
→ Root Cause Analysis → Severity Assessment → Report Generation → UI
```

---

## 📂 Project Structure

```
AI_DDR_Report/
│
├── app.py                 # Streamlit UI
├── main.py                # Pipeline orchestration
│
├── parser/
│   ├── pdf_parser.py
│   └── image_extractor.py
│
├── engine/
│   ├── rule_engine.py
│   ├── area_mapper.py
│   ├── deduplicator.py
│   ├── reasoning_engine.py
│   ├── severity_engine.py
│   ├── conflict_checker.py
│   └── report_builder.py
│
├── utils/
│   ├── constants.py
│   └── pdf_generator.py
```

---

## ⚙️ Installation

```bash
pip install streamlit pdfplumber pymupdf reportlab
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 📄 Output (DDR Structure)

The generated report includes:

1. Property Issue Summary
2. Area-wise Observations
3. Probable Root Cause
4. Severity Assessment (with reasoning)
5. Recommended Actions
6. Additional Notes
7. Missing / Unclear Information

---

## ⚠️ Key Design Principles

* No hallucination — only uses available data
* Handles missing information explicitly
* Avoids duplicate issues
* Modular pipeline design
* Easily extendable with LLMs

---

## 📌 Limitations

* Image-to-area mapping is basic (sequential)
* Rule-based system may miss complex context
* Thermal reasoning is heuristic

---

## 🔮 Future Improvements

* Intelligent image-to-area mapping
* Advanced NLP / LLM integration
* Improved thermal analysis
* Better PDF formatting (tables, layout)

---

## 👨‍💻 Author

Omkar
