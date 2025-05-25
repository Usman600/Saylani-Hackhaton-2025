import streamlit as st
from ocr import extract_text
from nlp_utils import parse_lab_results
from explain import explain_test_result
import os

st.title("🧬 AI Medical Report Assistant")

uploaded_file = st.file_uploader("Upload a scanned medical report (PDF/Image)", type=["png", "jpg", "jpeg", "pdf"])

if uploaded_file:
    os.makedirs("sample_reports", exist_ok=True)
    file_path = os.path.join("sample_reports", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    st.image(file_path, caption="Uploaded Report", use_container_width=True)

    with st.spinner("Extracting and analyzing..."):
        extracted_text = extract_text(file_path)
        st.text_area("Extracted Text", extracted_text, height=200)
        lab_results = parse_lab_results(extracted_text)

    if lab_results:
        for res in lab_results:
            st.subheader(res["test_name"].title())
            st.write(f"**Normal Range:** {res.get('normal_range', 'N/A')}")
            if res.get("description"):
                st.write(f"**Details:** {res['description']}")
            explanation = explain_test_result(
                res.get("test_name", "Unknown Test"),
                res.get("value", "N/A"),
                res.get("normal_range", "N/A")
            )
            st.success(explanation)

    else:
        st.warning("Could not detect standard lab result format, showing raw text instead.")
        st.text(extracted_text)
