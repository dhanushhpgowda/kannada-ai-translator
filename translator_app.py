import streamlit as st
import os
from dotenv import load_dotenv
from pypdf import PdfReader
from docx import Document
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage

# 1. Setup & Folders
load_dotenv()
if not os.path.exists("docs"):
    os.makedirs("docs")

# Initialize Gemini 2.5 Flash
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash", 
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.1 # Keep it low for high translation accuracy
)

# 2. Text Extraction Logic
def extract_text(uploaded_file):
    if uploaded_file.name.endswith(".pdf"):
        reader = PdfReader(uploaded_file)
        return "".join([page.extract_text() for page in reader.pages])
    elif uploaded_file.name.endswith(".docx"):
        doc = Document(uploaded_file)
        return "\n".join([para.text for para in doc.paragraphs])
    return None

# 3. Streamlit UI
st.set_page_config(page_title="Kannada AI Translator", layout="wide")
st.title("⚖️ Kannada to English Doc Translator")
st.markdown("---")

# Sidebar for file management
with st.sidebar:
    st.header("Upload Center")
    uploaded_file = st.file_uploader("Choose a Kannada PDF or DOCX", type=["pdf", "docx"])
    if st.button("Clear Docs Folder"):
        for f in os.listdir("docs"):
            os.remove(os.path.join("docs", f))
        st.success("Folder Emptied!")

if uploaded_file:
    # Save file to docs/
    with open(os.path.join("docs", uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Extract Kannada text
    kn_text = extract_text(uploaded_file)
    
    # Create two columns for a professional view
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Original Kannada")
        st.text_area("Source Content", kn_text, height=400)

    with col2:
        st.subheader("Understandable English")
        if st.button("🚀 Start AI Translation"):
            with st.spinner("Gemini is analyzing and translating..."):
                # Professional Translation Prompt
                prompt = (
                    "You are a professional legal and formal translator. Translate the following "
                    "Kannada text into clear, understandable, and fluent English. "
                    "Do not translate word-for-word; ensure the legal/formal meaning is preserved."
                    f"\n\nTEXT:\n{kn_text[:8000]}" # Gemini 2.5 has a huge window, but 8k is safe
                )
                
                result = llm.invoke([HumanMessage(content=prompt)]).content
                st.write(result)
                
                # Download Button
                st.download_button(
                    label="📥 Download English Translation",
                    data=result,
                    file_name=f"Translated_{uploaded_file.name.split('.')[0]}.txt",
                    mime="text/plain"
                )
        else:
            st.info("Click the button above to begin.")

else:
    st.info("Please upload a Kannada document to get started.")