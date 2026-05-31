# 🤖 JARVIS - Standalone Voice Assistant

**One-click download and run. Everything included. No setup required.**

## ✨ Features

- 🎤 **Voice Recognition** - Listen and execute commands naturally
- 🌐 **Web Integration** - Open websites and search the web
- 📺 **Screen Capture** - Take screenshots instantly
- 🖥️ **App Launcher** - Open applications with voice
- ⏰ **Time & Date** - Check time and date
- 🌤️ **Weather** - Get weather information
- 💬 **Natural Language** - Understands conversational commands
- 🎨 **Beautiful UI** - Modern, intuitive interface

## 🚀 Quick Start

### Windows
1. **Download** the repository as ZIP (green Code button)
2. **Extract** the folder
3. **Double-click** `JARVIS.bat`
4. **Wait** for first-time setup (installs dependencies)
5. **Enjoy!** 🎉

### macOS / Linux
1. **Download** the repository as ZIP
2. **Extract** the folder
3. **Open Terminal** in the folder
4. **Run**: `bash jarvis.sh`
5. **Enjoy!** 🎉

## 📖 Usage

### Voice Commands
1. Click **🎤 Listen**
2. Speak your command naturally
3. JARVIS responds instantly

### Text Commands
1. Type in the text field
2. Press **Enter** or click **Send**
3. JARVIS responds

## 💬 Example Commands

| Command | What it does |
|---------|-------------|
| "Hello" | Greet JARVIS |
| "What time is it?" | Get current time |
| "Take a screenshot" | Capture your screen |
| "Open notepad" | Launch notepad |
| "Search Python" | Search the web |
| "Weather in London" | Get weather info |
| "Visit YouTube" | Open YouTube |

## ⚙️ System Requirements

- **Python 3.8+** - [Download from python.org](https://www.python.org/downloads/)
- **Microphone** - Any working microphone
- **Internet Connection** - For voice recognition and web features
- **OS** - Windows 10+, macOS 10.14+, or Ubuntu 18.04+

## 🛠️ Customization

Edit `jarvis_config.json` to add:
- Your favorite applications
- Your favorite websites
- OpenWeather API key (for weather)
- Your preferred name

## 📋 Supported Commands

```
Greeting:
- "Hello" / "Hi"

Time & Date:
- "What time is it?"
- "What is the date?"

Applications:
- "Open notepad"
- "Open calculator"
- "Open browser"

Websites:
- "Visit google"
- "Visit youtube"
- "Visit github"

Web Search:
- "Search [query]"
- "Find [query]"

Weather:
- "Weather in [city]"

Screen:
- "Take a screenshot"
- "Show screen"
```

## 🐛 Troubleshooting

### "Microphone not detected"
- Check Windows/Mac/Linux microphone settings
- Allow permissions when prompted
- Test microphone in system settings
- Restart JARVIS

### "Dependencies won't install"
- Run as Administrator (Windows)
- Check internet connection
- Delete `__pycache__` folder and try again

### "Python not found"
- Install Python 3.8+ from python.org
- Add Python to PATH (Windows)
- Use `python3` command (macOS/Linux)

### Still having issues?
- Delete `__pycache__` folder
- Try running `install_and_run.py` manually
- Check that your microphone works in other apps

## 📁 File Structure

```
JARVIS/
├── JARVIS.bat                 (Windows launcher)
├── jarvis.sh                  (macOS/Linux launcher)
├── jarvis_main.py             (Main application)
├── install_and_run.py         (Installer & runner)
├── jarvis_config.json         (Configuration)
├── requirements.txt           (Python packages)
└── README.md                  (This file)
```

## ⌨️ Keyboard Shortcuts

| Key | Action |
|-----|--------|
| **Enter** | Send text command |
| **Tab** | Navigate between elements |
| **Escape** | Close dialogs |

## 🔒 Privacy

- All speech is processed with Google Speech API
- No personal data is stored
- Screenshots saved locally only
- Configuration file is local

## 💡 Tips for Best Results

1. **Speak Clearly** - Natural, clear speech works best
2. **Quiet Environment** - Minimize background noise
3. **Good Microphone** - Better mic = better recognition
4. **Check Internet** - Required for voice recognition
5. **Customize Config** - Add your favorite apps and websites

## 📥 Download

**[Click the green Code button above and select Download ZIP](https://github.com/arafatmoh76-byte/JARVIS)**

Then:
1. Extract the ZIP file
2. Open the folder
3. Run `JARVIS.bat` (Windows) or `jarvis.sh` (macOS/Linux)
4. Enjoy!

## 📜 License

MIT License - Free to use and modify

---

**Enjoy your personal AI assistant!** 🤖✨