# 💬 ChatGPT-like App with Streamlit (No LLM)

## 📌 Overview
This project is a simple ChatGPT-style chat application built using **Streamlit** in Python.  
It simulates a conversational interface **without using any external APIs or Large Language Models (LLMs)**.

---

## ✨ Features
- 💬 Chat interface using Streamlit components (`st.chat_message`, `st.chat_input`)
- 🧠 Local mock responses using a Python dictionary
- 🗂️ Session-based chat history using `st.session_state`
- ⚡ Streaming response effect (word-by-word typing simulation)
- 🚫 No external APIs or AI models required

---

## ⚙️ How It Works
1. The user enters a message in the chat input.
2. The app processes the input using a local function.
3. It checks a predefined dictionary for a matching response.
4. If a match is found → returns the response.
5. If not → returns a default fallback message.
6. The response is streamed word-by-word for a realistic chat experience.
7. All messages are stored and displayed using session state.

---

## 🚀 Run the App Locally

### 1. Install dependencies
```bash
pip install streamlit
```

### 2. Run the application
```bash
streamlit run chat_app.py
```

---

## 📂 Project Structure
```
chat_app.py   # Main Streamlit application
README.md     # Project documentation
```

---

## ✅ Requirements Checklist
- [x] No external LLMs or APIs used  
- [x] Built using Streamlit chat components  
- [x] Chat history persists during session  
- [x] Mock response logic implemented locally  
- [x] Runs successfully using Streamlit  

---

## 🎥 Demo
*(Add your YouTube demo link here)*

---

## 👩‍💻 Author
**Sue**
