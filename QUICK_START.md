# 🚀 JARVIS - Quick Start Guide

## ⚡ One-Click Launch

### Windows
1. **Download** the JARVIS folder (green Code button → Download ZIP)
2. **Extract** the ZIP file
3. **Double-click** `JARVIS.bat`
4. **Wait** for setup (first time takes 1-2 minutes)
5. **Enjoy!** JARVIS opens automatically 🎉

### macOS / Linux
1. **Download** the JARVIS folder
2. **Extract** the ZIP file
3. **Open Terminal** in the folder
4. **Run**: `bash jarvis.sh`
5. **Enjoy!** JARVIS opens automatically 🎉

## 🎤 Using JARVIS

### Voice Mode
```
1. Click the 🎤 Listen button
2. Speak your command naturally
3. JARVIS responds with voice and text
```

### Text Mode
```
1. Type your command in the text field
2. Press Enter or click Send
3. JARVIS responds instantly
```

## 📝 Quick Commands

**Try these first:**

- "Hello" → JARVIS greets you
- "What time is it?" → Current time
- "Take a screenshot" → Captures screen
- "Open notepad" → Opens notepad
- "Search cats" → Searches web for "cats"
- "Weather in New York" → Weather info
- "Visit YouTube" → Opens YouTube

## ⚙️ Setup Notes

### First Time?
- ✅ Dependencies install automatically
- ✅ Microphone permissions will prompt
- ✅ Everything is configured and ready
- ✅ Takes 1-2 minutes on first run

### Microphone Setup
- **Windows**: Allow microphone permissions when prompted
- **macOS**: Settings → Security & Privacy → Microphone
- **Linux**: Check your audio device settings

## 🔧 Optional: Customize

Edit `jarvis_config.json` to:
- Add favorite apps
- Add favorite websites
- Add weather API key
- Change your name

**Example:**
```json
{
    "user_name": "John",
    "apps": {
        "spotify": "spotify.exe"
    },
    "websites": {
        "reddit": "https://www.reddit.com"
    }
}
```

## ❓ Need Help?

### In JARVIS
- Click the **❓ Help** button
- Or say "Help"

### Common Issues

**Microphone not working?**
- Check system microphone in Settings
- Test microphone in another app
- Restart JARVIS

**Dependencies won't install?**
- Make sure Python 3.8+ is installed
- Run as Administrator (Windows)
- Check internet connection

**Still stuck?**
- Delete `__pycache__` folder
- Try running `install_and_run.py` manually
- Restart your computer

## 🎯 Pro Tips

1. **Voice Recognition**: Speak clearly and naturally
2. **Quiet Space**: Less background noise = better results
3. **Internet**: Required for voice recognition
4. **Text Mode**: Faster if microphone isn't working
5. **Customize**: Edit config for your favorite apps

## 📋 System Requirements

- Python 3.8 or higher
- Working microphone
- Internet connection
- Windows 10+, macOS 10.14+, or Linux

---

**Ready? Download JARVIS and start commanding your AI assistant!** 🤖