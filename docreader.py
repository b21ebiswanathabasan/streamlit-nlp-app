import streamlit as st
from docx import Document
import pandas as pd
import io

# Page configuration
st.set_page_config(page_title="File to Text Converter", page_icon="📄", layout="centered")
st.title("📄 Word / Excel to Text Converter")

# Upload file
uploaded_file = st.file_uploader("Upload a Word (.docx) or Excel (.xlsx) file", type=["docx", "xlsx"])

if uploaded_file:
    file_type = uploaded_file.name.split(".")[-1].lower()

    if file_type == "docx":
        try:
            doc = Document(uploaded_file)
            st.subheader("📃 Extracted Text from Word File:")
            for para in doc.paragraphs:
                if para.text.strip():
                    st.markdown(f"- {para.text}")
        except Exception as e:
            st.error(f"❌ Unable to read Word file: {e}")

    elif file_type == "xlsx":
        try:
            excel_data = pd.read_excel(uploaded_file, sheet_name=None)
            st.subheader("📊 Extracted Text from Excel File:")

            for sheet_name, df in excel_data.items():
                st.markdown(f"**🗂️ Sheet: {sheet_name}**")
                text_output = df.astype(str).fillna('').apply(lambda x: ' | '.join(x), axis=1)
                for line in text_output:
                    st.markdown(f"- {line}")
        except Exception as e:
            st.error(f"❌ Unable to read Excel file: {e}")
    else:
        st.warning("Unsupported file type. Please upload .docx or .xlsx.")
