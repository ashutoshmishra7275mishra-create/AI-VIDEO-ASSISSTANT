# 🎥 AI Video Assistant

An AI-powered Video Assistant that automatically downloads YouTube videos or processes local video/audio files, transcribes speech, generates summaries, extracts action items, and enables multilingual Question Answering using Retrieval-Augmented Generation (RAG).

---

## 🚀 Features

- 🎥 Process YouTube videos
- 📂 Process local audio/video files
- 🎙️ Speech-to-Text using Whisper & Sarvam AI
- 📝 Automatic Transcript Generation
- 📄 AI-Powered Summary
- 📌 AI-Generated Title
- ✅ Extract Action Items
- 🔑 Extract Key Decisions
- ❓ Extract Open Questions
- 🤖 RAG-based Question Answering
- 🌍 Multilingual Support
  - English
  - Hindi
  - Hinglish

---

## 🛠 Tech Stack

- Python
- LangChain
- Mistral AI
- OpenAI Whisper
- Sarvam AI
- ChromaDB
- HuggingFace Embeddings
- yt-dlp
- FFmpeg

---

## 📂 Project Structure

```
AI-VIDEO-ASSISSTANT
│
├── core/
│   ├── extractor.py
│   ├── rag_engine.py
│   ├── summarizer.py
│   ├── transcriber.py
│   └── vector_store.py
│
├── utils/
│   └── audio_processor.py
│
├── main.py
├── app.py
├── Requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/ashutoshmishra7275mishra-create/AI-VIDEO-ASSISSTANT.git

cd AI-VIDEO-ASSISSTANT
```

Install dependencies

```bash
pip install -r Requirements.txt
```

Install FFmpeg

```
winget install "FFmpeg (Essentials Build)"
```

Create a `.env` file

```env
SARVAM_API_KEY=YOUR_SARVAM_API_KEY
MISTRAL_API_KEY=YOUR_MISTRAL_API_KEY
```

---

## ▶️ Run

```bash
python main.py
```

Example

```
Enter YouTube URL or local file path:
https://www.youtube.com/watch?v=jNQXAC9IVRw
```

---

## 💬 Example Questions

### English

- What is this video about?
- Summarize the video.
- What are the key points?
- What did the speaker say?

### Hindi

- वीडियो किस बारे में है?
- सारांश बताइए।
- मुख्य बिंदु क्या हैं?

### Hinglish

- Video kis baare me hai?
- Summary batao.
- Speaker ne kya bola?

---

## 📸 Output

- Transcript
- AI Summary
- AI Title
- Action Items
- Key Decisions
- Open Questions
- Multilingual AI Chat

---

## 🎯 Future Improvements

- Streamlit Web UI
- PDF Export
- Timestamp-based Answers
- Speaker Diarization
- Chat History
- Semantic Search
- Multiple Video Support

---

## 👨‍💻 Author

**Ashutosh Mishra**

GitHub:
https://github.com/ashutoshmishra7275mishra-create

---

## ⭐ Support

If you like this project, don't forget to ⭐ Star the repository.
