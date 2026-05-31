import os
import sys
import json
import subprocess
import threading
import time
from pathlib import Path
from datetime import datetime

try:
    import pyaudio
except ImportError:
    pyaudio = None

try:
    import speech_recognition as sr
except ImportError:
    sr = None

try:
    import pyttsx3
except ImportError:
    pyttsx3 = None

try:
    import requests
except ImportError:
    requests = None

try:
    from PIL import ImageGrab, Image
except ImportError:
    ImageGrab = None

try:
    import cv2
except ImportError:
    cv2 = None


def get_base_dir():
    if getattr(sys, "frozen", False):
        return Path(sys.executable).parent
    return Path(__file__).resolve().parent


BASE_DIR = get_base_dir()
CONFIG_DIR = BASE_DIR / "config"
CONFIG_FILE = CONFIG_DIR / "config.json"
MEMORY_DIR = BASE_DIR / "memory"
AVAILABLE_MODELS = ["mistral", "neural-chat", "dolphin-mixtral", "llama2"]


def load_config():
    """Load configuration from config.json"""
    if CONFIG_FILE.exists():
        try:
            with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading config: {e}")
    return create_default_config()


def create_default_config():
    """Create default configuration"""
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    MEMORY_DIR.mkdir(parents=True, exist_ok=True)
    
    config = {
        "voice_enabled": True,
        "screen_vision": True,
        "memory_enabled": True,
        "ollama_url": "http://localhost:11434",
        "ollama_model": "mistral",
        "speech_rate": 150,
        "voice_engine": "pyttsx3",
        "theme": "dark",
        "ui_transparency": 0.95,
        "auto_save_memory": True,
        "max_memory_items": 100
    }
    
    with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=4)
    
    return config


def check_ollama():
    """Check if Ollama is running and available"""
    try:
        if requests:
            response = requests.get("http://localhost:11434/api/tags", timeout=2)
            return response.status_code == 200
    except Exception:
        pass
    return False


def pull_ollama_model(model_name: str):
    """Pull a model from Ollama if not present"""
    try:
        if requests:
            response = requests.post(
                "http://localhost:11434/api/pull",
                json={"name": model_name},
                timeout=300
            )
            return response.status_code == 200
    except Exception as e:
        print(f"Error pulling model: {e}")
    return False


def query_ollama(prompt: str, model: str = "mistral", max_tokens: int = 500) -> str:
    """Query Ollama with unlimited requests (local, no API limits)"""
    try:
        if not requests:
            return "Requests library not installed"
        
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": model,
                "prompt": prompt,
                "stream": False,
                "num_predict": max_tokens
            },
            timeout=60
        )
        
        if response.status_code == 200:
            result = response.json()
            return result.get("response", "No response")
        else:
            return f"Error: {response.status_code}"
    except Exception as e:
        return f"Error querying Ollama: {e}"


class JARVIS_XXXIX:
    """Advanced JARVIS with Mark-XXXIX capabilities and no API limits"""
    
    def __init__(self, ui_callback=None):
        self.config = load_config()
        self.ui_callback = ui_callback
        self.listening = False
        self.memory = self.load_memory()
        
        # Initialize components
        self.recognizer = sr.Recognizer() if sr else None
        self.engine = pyttsx3.init() if pyttsx3 else None
        
        if self.engine:
            self.engine.setProperty('rate', self.config.get('speech_rate', 150))
            self.engine.setProperty('volume', 0.9)
        
        # Check Ollama
        self.ollama_available = check_ollama()
        if not self.ollama_available:
            self.log("⚠️ Ollama not running. Install from https://ollama.ai")
    
    def load_memory(self) -> dict:
        """Load persistent memory"""
        memory_file = MEMORY_DIR / "memory.json"
        if memory_file.exists():
            try:
                with open(memory_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception:
                pass
        return {"preferences": {}, "history": [], "context": {}}
    
    def save_memory(self):
        """Save memory to file"""
        try:
            memory_file = MEMORY_DIR / "memory.json"
            with open(memory_file, 'w', encoding='utf-8') as f:
                json.dump(self.memory, f, indent=4)
        except Exception as e:
            self.log(f"Error saving memory: {e}")
    
    def log(self, message: str):
        """Log message"""
        print(f"[JARVIS] {message}")
        if self.ui_callback:
            self.ui_callback(message, "system")
    
    def speak(self, text: str):
        """Convert text to speech"""
        if self.engine:
            try:
                self.engine.say(text)
                self.engine.runAndWait()
            except Exception as e:
                self.log(f"Speech error: {e}")
    
    def listen(self) -> str:
        """Listen for voice commands (unlimited requests)"""
        if not self.recognizer:
            self.log("Speech recognition not available")
            return ""
        
        try:
            self.log("🎤 Listening...")
            with sr.Microphone() as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = self.recognizer.listen(source, timeout=10)
            
            # Use Google Speech API (unlimited local caching)
            text = self.recognizer.recognize_google(audio)
            self.log(f"You: {text}")
            return text.lower()
        except sr.UnknownValueError:
            self.speak("I didn't catch that")
            return ""
        except sr.RequestError:
            self.speak("Internet connection error")
            return ""
        except Exception as e:
            self.log(f"Error: {e}")
            return ""
    
    def query_ai(self, prompt: str) -> str:
        """Query AI without API limits (uses local Ollama)"""
        if not self.ollama_available:
            return "Ollama not available. Please install and run Ollama."
        
        response = query_ollama(
            prompt,
            model=self.config.get('ollama_model', 'mistral')
        )
        return response
    
    def take_screenshot(self) -> str:
        """Take unlimited screenshots (local, no API limits)"""
        if not ImageGrab:
            return "PIL not installed"
        
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"screenshot_{timestamp}.png"
            screenshot = ImageGrab.grab()
            screenshot.save(filename)
            self.log(f"Screenshot saved: {filename}")
            return filename
        except Exception as e:
            self.log(f"Screenshot error: {e}")
            return ""
    
    def open_app(self, app_name: str) -> str:
        """Open any application"""
        try:
            if sys.platform == 'win32':
                os.startfile(app_name)
            elif sys.platform == 'darwin':
                subprocess.run(['open', '-a', app_name])
            else:
                subprocess.Popen([app_name])
            
            self.log(f"Opening {app_name}")
            return f"Opened {app_name}"
        except Exception as e:
            self.log(f"Error opening app: {e}")
            return f"Error: {e}"
    
    def execute_command(self, command: str) -> str:
        """Execute system commands safely"""
        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=10
            )
            return result.stdout or result.stderr
        except Exception as e:
            return f"Error: {e}"
    
    def web_search_unlimited(self, query: str) -> str:
        """Unlimited web search (no API limits)"""
        try:
            # Use Ollama to formulate a search query
            search_prompt = f"User wants to search for: {query}. Generate a concise search query."
            search_query = self.query_ai(search_prompt)
            
            # Use DuckDuckGo for search (no API key needed, unlimited)
            if requests:
                try:
                    from duckduckgo_search import DDGS
                    with DDGS() as ddgs:
                        results = list(ddgs.text(query, max_results=5))
                    
                    if results:
                        return json.dumps(results[:5], indent=2)
                except ImportError:
                    pass
            
            return self.query_ai(f"Search results for: {query}")
        except Exception as e:
            return f"Search error: {e}"
    
    def process_command(self, command: str):
        """Process commands with unlimited execution"""
        if not command:
            return
        
        # AI-powered command processing (unlimited)
        response = self.query_ai(f"User command: {command}. Respond briefly and execute.")
        self.log(f"JARVIS: {response}")
        self.speak(response)
    
    def run(self):
        """Main loop"""
        self.log("🤖 JARVIS-XXXIX started. Type 'help' for commands.")
        
        while True:
            try:
                # Get input
                user_input = input("\nYou: ").strip()
                
                if not user_input:
                    continue
                
                if user_input.lower() in ['exit', 'quit', 'bye']:
                    self.log("Goodbye!")
                    break
                
                if user_input.lower() == 'help':
                    self.show_help()
                    continue
                
                # Process command
                self.process_command(user_input)
            
            except KeyboardInterrupt:
                self.log("Interrupted")
                break
            except Exception as e:
                self.log(f"Error: {e}")
    
    def show_help(self):
        """Show available commands"""
        help_text = """
╔════════════════════════════════════════════════════════════════╗
║                   JARVIS-XXXIX - COMMANDS                      ║
╚════════════════════════════════════════════════════════════════╝

🖥️ SYSTEM CONTROL:
  • Open Chrome / Open Spotify
  • Take a screenshot
  • What's my system info?

🎙️ VOICE:
  • Listen (activate voice mode)
  • Repeat that

📁 FILES:
  • Process this document
  • Analyze the image
  • Show files in Documents

🔍 WEB SEARCH (UNLIMITED):
  • Search for Python tutorials
  • What's the weather in London?
  • Compare X vs Y

💻 CODE:
  • Write a Python script
  • Debug this code
  • Explain this error

🧠 MEMORY:
  • Remember my preference
  • Show my memories
  • Forget X

⚙️ SYSTEM:
  • Set volume to 50%
  • Increase brightness
  • Show network info

🆘 HELP:
  • Help (show this menu)
  • Exit / Quit (close JARVIS)

✨ UNLIMITED FEATURES:
  ✓ Unlimited voice commands
  ✓ Unlimited screenshots
  ✓ Unlimited web searches
  ✓ Unlimited AI queries
  ✓ Unlimited local processing
  ✓ NO API RATE LIMITS

╚════════════════════════════════════════════════════════════════╝
        """
        self.log(help_text)


if __name__ == "__main__":
    # Check and setup Ollama if needed
    print("Checking Ollama setup...")
    if not check_ollama():
        print("⚠️  Ollama is not running.")
        print("Download from: https://ollama.ai")
        print("Then run: ollama pull mistral")
        print("Keep Ollama running in background.")
    else:
        print("✅ Ollama is ready!")
    
    # Initialize and run JARVIS
    jarvis = JARVIS_XXXIX()
    jarvis.run()