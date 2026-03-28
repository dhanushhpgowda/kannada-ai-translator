🌐 Kannada AI Translator

An AI-powered web application that translates Kannada documents (PDF/DOCX) into clear and natural English using Google Gemini.

---

🚀 Features

- 📄 Upload Kannada PDF or DOCX files
- 🔍 Automatic text extraction
- 🤖 AI-powered translation
- 🌐 Context-aware and fluent English output
- 📥 Download translated text
- 🧹 Clear uploaded files option

---

🛠️ Tech Stack

- Python
- Streamlit
- Google Generative AI (Gemini)
- LangChain
- PyPDF
- python-docx

---

📂 Project Structure

kannada-ai-translator/
│── app.py
│── docs/
│── requirements.txt
│── .env
│── .gitignore
│── README.md

---

⚙️ Setup Instructions

1. Clone the Repository

git clone https://github.com/your-username/kannada-ai-translator.git
cd kannada-ai-translator

2. Install Dependencies

pip install -r requirements.txt

3. Add API Key

Create a ".env" file in the root directory:

GOOGLE_API_KEY=your_api_key_here

4. Run the App

streamlit run app.py

---

🧠 How It Works

1. Upload a Kannada document (PDF/DOCX)
2. Extract text using PyPDF / python-docx
3. Send content to Gemini AI
4. Get translated English output
5. Download the result

---

🎯 Future Improvements

- 🌍 Multi-language support
- 📝 Text summarization
- 🎙️ Voice input/output
- 📊 UI enhancements

---

⚠️ Notes

- Works best with text-based PDFs (not scanned images)
- Requires a valid Google API key

---

👨‍💻 Author

Dhanush P

---

⭐ Support

If you like this project, consider giving it a star ⭐