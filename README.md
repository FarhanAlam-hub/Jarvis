# 🤖 Jarvis - Voice Assistant

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey?logo=windows)

**A voice-activated personal assistant built with Python, powered by AI**

*Inspired by Iron Man's JARVIS — listens for a wake word, understands your commands, and responds intelligently.*

</div>

---

## 📖 Overview

Jarvis is a desktop voice assistant that listens for the wake word **"Jarvis"**, then processes voice commands using speech recognition and responds using text-to-speech. It integrates with **Groq's AI API** to answer general knowledge questions and can perform tasks like opening websites directly in your preferred browser.

<!-- 
📸 Add a demo screenshot or GIF here! 
Example: ![Jarvis Demo](assets/demo.gif)
Record a short terminal session using a tool like ScreenToGif or Peek, save it in an `assets/` folder, and reference it above.
-->

## ✨ Features

- 🎙️ **Wake Word Detection** — Activates on hearing "Jarvis"
- 🗣️ **Voice Command Recognition** — Uses Google Speech Recognition to understand spoken commands
- 🔊 **Text-to-Speech Replies** — Responds audibly using `pyttsx3`
- 🧠 **AI-Powered Q&A** — Answers general questions using Groq's LLM API (OpenAI-compatible)
- 🌐 **Browser Automation** — Opens websites (e.g., Google) directly in Brave browser
- ⚙️ **Configurable Voice** — Switch between available system voices (male/female)

## 🖼️ Screenshots
<div align = "center">
  <img src="jarvis_pic.png" alt="Jarvis listening mode" width="700">
  <p><em>Jarvis actively listening for a command</em></p>
</div>
<!-- 
📸 Replace these placeholders with real screenshots of your project running.
Take a screenshot of your terminal while Jarvis is listening/responding,
save it as assets/screenshot1.png, and update the path below.
-->

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Language | Python 3.10+ |
| Speech-to-Text | `SpeechRecognition` (Google Speech API) |
| Text-to-Speech | `pyttsx3` |
| AI Model | Groq API (`openai/gpt-oss-20b`) |
| Browser Automation | `webbrowser` module |

## 📂 Project Structure

```
Jarvis/
├── Jarvis/
│   ├── main.py          # Core assistant loop (wake word + commands)
│   └── client.py        # Groq AI API client
├── .venv/                # Virtual environment (not committed)
├── requirements.txt
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- A microphone
- [Brave Browser](https://brave.com/) installed (or update the path for your preferred browser)
- A free [Groq API key](https://console.groq.com/)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/jarvis.git
   cd jarvis
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\Activate.ps1      # Windows PowerShell
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set your Groq API key as an environment variable**
   ```powershell
   [System.Environment]::SetEnvironmentVariable('GROQ_API_KEY', 'your-key-here', 'User')
   ```
   > ⚠️ Never hardcode your API key in the source code or commit it to GitHub.

5. **Run Jarvis**
   ```bash
   python Jarvis/main.py
   ```

### `requirements.txt`

```
speechrecognition
pyttsx3
openai
requests
pyaudio
```

## 🎯 Usage

1. Run the script — Jarvis initializes and starts listening.
2. Say **"Jarvis"** to activate it.
3. Once it replies "Yes Sir", speak your command:
   - *"Open Google"* → opens Google in Brave
   - Ask any general question → answered via Groq AI

## 🗺️ Roadmap

- [ ] Add more voice commands (YouTube, GitHub, LinkedIn, etc.)
- [ ] Wake word detection using offline models (e.g., Porcupine) instead of cloud STT
- [ ] GUI interface
- [ ] Local LLM support via Ollama for fully offline operation
- [ ] Custom wake word training

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](../../issues).

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Groq](https://groq.com/) for blazing-fast free AI inference
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) library
- [pyttsx3](https://pypi.org/project/pyttsx3/) for offline text-to-speech

---

<div align="center">
Made with ❤️ by <a href="https://github.com/<your-username>">Farhan</a>
</div>
