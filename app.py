from utils.pdf_generator import generate_pdf
import streamlit as st
from main import run_pipeline
import tempfile

st.set_page_config(page_title="AI DDR Report Generator")

st.title("DDR Report Generator")
st.write("Upload inspection and thermal reports to generate analysis.")

inspection_file = st.file_uploader("Upload Inspection Report", type=["pdf"])
thermal_file = st.file_uploader("Upload Thermal Report", type=["pdf"])

if st.button("Generate Report"):
    if inspection_file and thermal_file:

        import tempfile

        with tempfile.NamedTemporaryFile(delete=False) as f1:
            f1.write(inspection_file.read())
            inspection_path = f1.name

        with tempfile.NamedTemporaryFile(delete=False) as f2:
            f2.write(thermal_file.read())
            thermal_path = f2.name

        with st.spinner("Processing..."):
            report, area_data, images = run_pipeline(inspection_path, thermal_path)

        st.success("Report Generated!")

        # ✅ Show report
        st.markdown(report)

        # ✅ Show images
        st.subheader("📸 Inspection Images")
        for img in images:
            st.image(img)

        # ✅ Generate PDF
        pdf_path = generate_pdf(report, images)

        with open(pdf_path, "rb") as f:
            st.download_button(
                label="📥 Download Report as PDF",
                data=f,
                file_name="DDR_Report.pdf",
                mime="application/pdf"
            )
    else:
        st.warning("Please upload both files.")