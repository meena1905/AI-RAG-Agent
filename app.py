import streamlit as st
import tempfile
import os
from rag_pipeline import create_rag

st.title("📄 AI PDF RAG Assistant")

# File upload
uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

if uploaded_file is not None:
    # Use temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        temp_pdf_path = tmp_file.name

    # Create RAG chain (session state)
    if "qa_chain" not in st.session_state:
        with st.spinner("Processing PDF and building index..."):
            st.session_state.qa_chain = create_rag(temp_pdf_path)
    
    # Clean up temp file
    try:
        os.unlink(temp_pdf_path)
    except:
        pass

    # Question input
    question = st.text_input("Ask a question about the PDF:")
    
    if question:
        with st.spinner("Generating answer..."):
            # ✅ FIXED: New Runnable chain takes direct string input
            answer = st.session_state.qa_chain.invoke(question)  # Direct string!

        st.subheader("Answer")
        st.write(answer)
