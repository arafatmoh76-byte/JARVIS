# 🤖 JARVIS-XXXIX - Advanced Computer Control AI

> **The most advanced version of JARVIS - Without API limits. Local execution. Total freedom.**

A real-time voice AI that can hear, see, understand, and control your computer — on any OS. Supporting Windows, macOS, and Linux. **Zero API rate limits. Unlimited usage.**

---

## ✨ Overview

JARVIS-XXXIX is an advanced AI assistant that bridges the gap between the operating system and human intent. Through natural dialogue, JARVIS analyzes your screen, processes documents, and executes complex workflows with an adaptive, beautiful interface.

Unlike other AI assistants, **JARVIS-XXXIX runs locally with no API rate limits** — use it as much as you want, whenever you want.

---

## 🚀 Capabilities

### Core Features
| Feature | Description |
|---|---|
| 🎙️ Real-time Voice | Ultra-low latency conversation with speech recognition |
| 🖥️ System Control | Launch apps, manage files, execute terminal commands |
| 👁️ Screen Vision | Real-time screen capture and analysis |
| 📁 File Processing | Upload, analyze, and process documents and code |
| 🧠 Local AI | Uses Ollama/Open models - no cloud dependencies |
| ⌨️ Hybrid Input | Voice commands + text input |
| 💾 Memory | Remembers your preferences and context |
| 🌐 Web Access | Search the web without API limits |
| 📊 System Info | Monitor CPU, RAM, network in real-time |
| 🎮 App Control | Launch, close, and interact with applications |

---

## 🆕 What's New

- ✅ **No API Rate Limits** - Use freely and unlimited times
- ✅ **Local Models** - Run on your machine with Ollama
- ✅ **Advanced UI** - Beautiful, responsive interface with real-time stats
- ✅ **Screen Vision** - See and analyze your screen in real-time
- ✅ **File Management** - Process PDFs, images, code, documents
- ✅ **Memory System** - Persistent context and preferences
- ✅ **Cross-Platform** - Windows, macOS, Linux fully supported
- ✅ **Code Helper** - Write, debug, and run code
- ✅ **Web Search** - Unlimited searches without API limits
- ✅ **Desktop Control** - Full computer automation

---

## ⚡ Quick Start

### 1. Download & Extract
```bash
git clone https://github.com/arafatmoh76-byte/JARVIS-XXXIX.git
cd JARVIS-XXXIX
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Setup Ollama (for local AI)
- Download from: https://ollama.ai
- Run: `ollama pull mistral`
- Keep Ollama running in background

### 4. Run JARVIS
```bash
python main.py
```

---

## 📋 System Requirements

| Requirement | Details |
|---|---|
| **OS** | Windows 10/11, macOS, or Linux |
| **Python** | 3.9 or higher |
| **RAM** | 8GB minimum (16GB recommended) |
| **Microphone** | Required for voice |
| **Ollama** | Free, local AI (optional for advanced features) |

---

## 🎙️ How to Use

### Voice Commands
1. Click **🎤 Listen** or press `Space`
2. Speak naturally
3. JARVIS responds with voice and actions

### Text Commands
1. Type in the command box
2. Press **Enter**
3. JARVIS executes immediately

---

## 📝 Example Commands

```
Screen & Vision:
• "What's on my screen?"
• "Read this PDF for me"
• "Analyze the image"

App Control:
• "Open Chrome"
• "Close all windows"
• "Launch Spotify"

System Control:
• "Set volume to 50%"
• "Increase brightness"
• "Turn on WiFi"
• "Show system info"

Web & Search:
• "Search for Python tutorials"
• "What's the weather in London?"
• "Compare Python vs JavaScript"

Code & Files:
• "Write a Python script to rename files"
• "Debug this code"
• "Create a folder structure"

Memory & Context:
• "Remember my favorite color is blue"
• "What did I ask you yesterday?"
• "Show my preferences"
```

---

## 🔧 Configuration

Edit `config.json`:

```json
{
    "voice_enabled": true,
    "screen_vision": true,
    "memory_enabled": true,
    "ollama_url": "http://localhost:11434",
    "ollama_model": "mistral",
    "speech_rate": 150
}
```

---

## 🎨 UI Features

- ✅ Real-time system metrics (CPU, RAM, Network)
- ✅ Draggable file upload area
- ✅ Transparent chat interface
- ✅ Command history
- ✅ Keyboard shortcuts
- ✅ Customizable colors and layout
- ✅ Responsive design

---

## 🛠️ Troubleshooting

### "Microphone not detected"
- Check system microphone settings
- Allow permissions when prompted
- Run as Administrator (Windows)

### "Ollama connection failed"
- Download Ollama: https://ollama.ai
- Run: `ollama pull mistral`
- Ensure Ollama is running

### "ModuleNotFoundError"
```bash
pip install -r requirements.txt
```

---

## 📚 Project Structure

```
JARVIS-XXXIX/
├── main.py                 # Main entry point
├── ui.py                   # PyQt6 interface
├── config.json            # Configuration
├── requirements.txt       # Dependencies
├── core/
│   ├── prompt.txt        # System prompt
│   └── engine.py         # AI engine (local models)
├── actions/
│   ├── screen_processor.py   # Screen vision
│   ├── file_processor.py     # File handling
│   ├── open_app.py          # App control
│   ├── computer_settings.py  # System control
│   ├── web_search.py        # Web search (unlimited)
│   ├── code_helper.py       # Code generation
│   ├── desktop.py           # Desktop control
│   └── ...
├── memory/
│   └── memory_manager.py  # Context & preferences
└── utils/
    ├── audio.py          # Voice I/O
    └── system.py         # System utilities
```

---

## 🔒 Privacy & Security

✅ **Everything runs locally** - No cloud processing  
✅ **No API dependencies** - Complete independence  
✅ **Your data stays yours** - Nothing uploaded  
✅ **Open source** - Transparent and auditable  

---

## 📊 Performance

- **Voice Response**: < 500ms (local processing)
- **Screen Vision**: Real-time (< 1 second)
- **File Processing**: Instant (no cloud wait)
- **Memory**: Persistent & instant recall

---

## 🎓 Advanced Features

### Custom Commands
Edit `core/prompt.txt` to teach JARVIS new behaviors.

### Memory System
Automatically remembers user preferences, project context, and personal information.

### Code Integration
Generate, debug, and execute Python code safely in sandboxed environment.

### Desktop Automation
Create complex workflows with multi-step automation.

---

## 📜 License

MIT License - Free to use and modify

---

## 🚀 What's Next?

1. Download JARVIS-XXXIX
2. Install Ollama for local AI
3. Run and start commanding
4. Customize for your workflow
5. Never worry about API limits again!

---

**Experience the future of desktop AI. Unlimited. Local. Yours.** 🤖✨