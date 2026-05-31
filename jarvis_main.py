import os
import sys
import json
import subprocess
import webbrowser
import pyttsx3
import speech_recognition as sr
from datetime import datetime
from PIL import ImageGrab, Image
import requests
import threading
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from PIL import ImageTk
import traceback

# Initialize text-to-speech engine
try:
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 0.9)
except Exception as e:
    print(f"Warning: Text-to-speech initialization failed: {e}")
    engine = None

class JARVIS:
    def __init__(self, ui_callback=None):
        self.recognizer = sr.Recognizer()
        self.recognizer.energy_threshold = 4000
        self.running = True
        self.config = self.load_config()
        self.ui_callback = ui_callback
        
    def load_config(self):
        """Load configuration from config file"""
        config_file = 'jarvis_config.json'
        if os.path.exists(config_file):
            with open(config_file, 'r') as f:
                return json.load(f)
        return self.create_default_config()
    
    def create_default_config(self):
        """Create default configuration"""
        if sys.platform == 'win32':
            apps = {
                'notepad': 'notepad.exe',
                'calculator': 'calc.exe',
                'browser': 'chrome',
            }
        elif sys.platform == 'darwin':  # macOS
            apps = {
                'notepad': 'TextEdit',
                'calculator': 'Calculator',
                'browser': 'Safari',
            }
        else:  # Linux
            apps = {
                'notepad': 'gedit',
                'calculator': 'gnome-calculator',
                'browser': 'firefox',
            }
        
        config = {
            'apps': apps,
            'websites': {
                'google': 'https://www.google.com',
                'youtube': 'https://www.youtube.com',
                'github': 'https://www.github.com',
                'twitter': 'https://www.twitter.com',
                'stackoverflow': 'https://www.stackoverflow.com'
            },
            'openweather_api': 'YOUR_API_KEY_HERE',
            'user_name': 'sir'
        }
        with open('jarvis_config.json', 'w') as f:
            json.dump(config, f, indent=4)
        return config
    
    def speak(self, text):
        """Convert text to speech"""
        if self.ui_callback:
            self.ui_callback(f"JARVIS: {text}", "jarvis")
        
        if engine:
            try:
                engine.say(text)
                engine.runAndWait()
            except Exception as e:
                print(f"Speech error: {e}")
    
    def listen(self):
        """Listen to user voice command"""
        try:
            if self.ui_callback:
                self.ui_callback("🎤 Listening...", "system")
            
            with sr.Microphone() as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = self.recognizer.listen(source, timeout=10)
            
            text = self.recognizer.recognize_google(audio)
            if self.ui_callback:
                self.ui_callback(f"You: {text}", "user")
            return text.lower()
        except sr.UnknownValueError:
            self.speak("Sorry, I didn't understand that. Could you please repeat?")
            return None
        except sr.RequestError:
            self.speak("Sorry, I'm having trouble connecting to the internet.")
            return None
        except Exception as e:
            if self.ui_callback:
                self.ui_callback(f"Microphone Error: {str(e)}", "error")
            return None
    
    def open_app(self, app_name):
        """Open applications"""
        apps = self.config['apps']
        if app_name in apps:
            try:
                if sys.platform == 'darwin':  # macOS
                    subprocess.Popen(['open', '-a', apps[app_name]])
                else:
                    subprocess.Popen(apps[app_name])
                self.speak(f"Opening {app_name}")
            except Exception as e:
                self.speak(f"Sorry, I couldn't open {app_name}.")
        else:
            self.speak(f"I don't know how to open {app_name}")
    
    def open_website(self, website_name):
        """Open websites"""
        websites = self.config['websites']
        if website_name in websites:
            try:
                webbrowser.open(websites[website_name])
                self.speak(f"Opening {website_name}")
            except Exception as e:
                self.speak(f"Error opening {website_name}.")
        else:
            try:
                webbrowser.open(f"https://www.{website_name}.com")
                self.speak(f"Opening {website_name}")
            except Exception as e:
                self.speak(f"Error opening {website_name}.")
    
    def take_screenshot(self):
        """Capture and display screenshot"""
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"screenshot_{timestamp}.png"
            screenshot = ImageGrab.grab()
            screenshot.save(filename)
            self.speak(f"Screenshot saved as {filename}")
            return filename
        except Exception as e:
            self.speak(f"Error taking screenshot: {str(e)}")
            return None
    
    def search_web(self, query):
        """Search the web"""
        try:
            url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
            webbrowser.open(url)
            self.speak(f"Searching for {query}")
        except Exception as e:
            self.speak(f"Error searching: {str(e)}")
    
    def get_weather(self, city='London'):
        """Get weather information"""
        try:
            api_key = self.config.get('openweather_api')
            if api_key == 'YOUR_API_KEY_HERE':
                self.speak("Please set your OpenWeather API key in the config file for weather updates")
                return
            
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
            response = requests.get(url, timeout=5)
            data = response.json()
            
            if response.status_code == 200:
                temp = data['main']['temp']
                description = data['weather'][0]['description']
                self.speak(f"The weather in {city} is {description} with a temperature of {temp} degrees Celsius")
            else:
                self.speak(f"I couldn't find weather information for {city}")
        except Exception as e:
            self.speak(f"Error getting weather: {str(e)}")
    
    def tell_time(self):
        """Tell the current time"""
        current_time = datetime.now().strftime("%I:%M %p")
        self.speak(f"The current time is {current_time}")
    
    def tell_date(self):
        """Tell the current date"""
        current_date = datetime.now().strftime("%A, %B %d, %Y")
        self.speak(f"Today is {current_date}")
    
    def process_command(self, command):
        """Process user commands"""
        if not command:
            return
        
        if 'hello' in command or 'hi' in command:
            self.speak(f"Hello {self.config['user_name']}, how can I help you?")
        elif 'what time' in command or 'tell me time' in command:
            self.tell_time()
        elif 'what date' in command or 'tell me date' in command:
            self.tell_date()
        elif 'open' in command:
            for app in self.config['apps'].keys():
                if app in command:
                    self.open_app(app)
                    return
            website = command.replace('open', '').strip()
            self.open_website(website)
        elif 'screenshot' in command or 'take a screenshot' in command or 'show screen' in command:
            self.take_screenshot()
        elif 'search' in command or 'find' in command:
            search_query = command.replace('search', '').replace('find', '').strip()
            self.search_web(search_query)
        elif 'weather' in command:
            city = command.replace('weather', '').replace('in', '').strip()
            if city:
                self.get_weather(city)
            else:
                self.get_weather()
        elif 'visit' in command or 'go to' in command:
            website = command.replace('visit', '').replace('go to', '').strip()
            self.open_website(website)
        else:
            self.speak("I'm not sure what you mean. Would you like me to help you?")


class JARVIS_UI:
    def __init__(self, root):
        self.root = root
        self.root.title("JARVIS - Voice Assistant")
        self.root.geometry("1000x700")
        self.root.configure(bg="#0a0e27")
        
        self.root.resizable(True, True)
        
        self.jarvis = JARVIS(ui_callback=self.add_message)
        self.listening = False
        
        self.setup_styles()
        self.create_ui()
        
    def setup_styles(self):
        """Setup ttk styles"""
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TButton', background="#0a0e27", foreground="#00d4ff")
        style.configure('TLabel', background="#0a0e27", foreground="#00d4ff")
        style.configure('TFrame', background="#0a0e27")
    
    def create_ui(self):
        """Create the main UI"""
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Header
        header_frame = ttk.Frame(main_frame)
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        title_label = ttk.Label(header_frame, text="🤖 JARVIS", font=("Arial", 28, "bold"))
        title_label.pack(side=tk.LEFT)
        
        subtitle_label = ttk.Label(header_frame, text="Just A Rather Very Intelligent System", font=("Arial", 12, "italic"))
        subtitle_label.pack(side=tk.LEFT, padx=(20, 0))
        
        # Chat display area
        chat_frame = ttk.Frame(main_frame)
        chat_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        self.chat_display = scrolledtext.ScrolledText(
            chat_frame,
            height=20,
            width=80,
            bg="#1a1f3a",
            fg="#00d4ff",
            font=("Courier", 10),
            wrap=tk.WORD,
            state=tk.DISABLED
        )
        self.chat_display.pack(fill=tk.BOTH, expand=True)
        
        # Configure text tags
        self.chat_display.tag_config("user", foreground="#00ff00", font=("Courier", 10, "bold"))
        self.chat_display.tag_config("jarvis", foreground="#00d4ff", font=("Courier", 10, "bold"))
        self.chat_display.tag_config("system", foreground="#ffaa00", font=("Courier", 10))
        self.chat_display.tag_config("error", foreground="#ff4444", font=("Courier", 10, "bold"))
        
        # Control panel
        control_frame = ttk.Frame(main_frame)
        control_frame.pack(fill=tk.X, pady=10)
        
        # Buttons frame
        button_frame = ttk.Frame(control_frame)
        button_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.listen_btn = tk.Button(
            button_frame,
            text="🎤 Listen",
            command=self.start_listening,
            bg="#00d4ff",
            fg="#0a0e27",
            font=("Arial", 12, "bold"),
            padx=20,
            pady=10,
            relief=tk.RAISED,
            cursor="hand2"
        )
        self.listen_btn.pack(side=tk.LEFT, padx=5)
        
        screenshot_btn = tk.Button(
            button_frame,
            text="📸 Screenshot",
            command=self.take_screenshot,
            bg="#00d4ff",
            fg="#0a0e27",
            font=("Arial", 12, "bold"),
            padx=20,
            pady=10,
            relief=tk.RAISED,
            cursor="hand2"
        )
        screenshot_btn.pack(side=tk.LEFT, padx=5)
        
        help_btn = tk.Button(
            button_frame,
            text="❓ Help",
            command=self.show_help,
            bg="#00d4ff",
            fg="#0a0e27",
            font=("Arial", 12, "bold"),
            padx=20,
            pady=10,
            relief=tk.RAISED,
            cursor="hand2"
        )
        help_btn.pack(side=tk.LEFT, padx=5)
        
        clear_btn = tk.Button(
            button_frame,
            text="🗑️ Clear",
            command=self.clear_chat,
            bg="#00d4ff",
            fg="#0a0e27",
            font=("Arial", 12, "bold"),
            padx=20,
            pady=10,
            relief=tk.RAISED,
            cursor="hand2"
        )
        clear_btn.pack(side=tk.LEFT, padx=5)
        
        # Input frame
        input_frame = ttk.Frame(control_frame)
        input_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(input_frame, text="Type command:").pack(side=tk.LEFT, padx=(0, 10))
        
        self.input_entry = ttk.Entry(input_frame, font=("Arial", 10))
        self.input_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        self.input_entry.bind('<Return>', lambda e: self.process_text_command())
        
        send_btn = tk.Button(
            input_frame,
            text="Send",
            command=self.process_text_command,
            bg="#00d4ff",
            fg="#0a0e27",
            font=("Arial", 10, "bold"),
            padx=15,
            pady=5,
            relief=tk.RAISED,
            cursor="hand2"
        )
        send_btn.pack(side=tk.LEFT)
        
        # Status bar
        status_frame = ttk.Frame(main_frame)
        status_frame.pack(fill=tk.X, pady=(10, 0))
        
        self.status_label = ttk.Label(status_frame, text="Ready 🟢", font=("Arial", 10))
        self.status_label.pack(side=tk.LEFT)
        
        # Welcome message
        self.add_message("Welcome to JARVIS! Click 'Listen' to start or type commands below.", "system")
    
    def add_message(self, message, msg_type="system"):
        """Add message to chat display"""
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.insert(tk.END, f"\n{message}", msg_type)
        self.chat_display.see(tk.END)
        self.chat_display.config(state=tk.DISABLED)
        self.root.update()
    
    def start_listening(self):
        """Start listening in a separate thread"""
        if not self.listening:
            self.listening = True
            self.listen_btn.config(bg="#ff4444")
            self.status_label.config(text="Listening 🔴")
            
            thread = threading.Thread(target=self.listen_thread)
            thread.daemon = True
            thread.start()
    
    def listen_thread(self):
        """Thread for listening"""
        try:
            command = self.jarvis.listen()
            if command:
                self.jarvis.process_command(command)
        except Exception as e:
            self.add_message(f"Error: {str(e)}", "error")
        finally:
            self.listening = False
            self.listen_btn.config(bg="#00d4ff")
            self.status_label.config(text="Ready 🟢")
    
    def process_text_command(self):
        """Process text command from input"""
        command = self.input_entry.get().strip()
        if command:
            self.add_message(f"You: {command}", "user")
            self.input_entry.delete(0, tk.END)
            self.jarvis.process_command(command)
    
    def take_screenshot(self):
        """Take a screenshot"""
        thread = threading.Thread(target=self.jarvis.take_screenshot)
        thread.daemon = True
        thread.start()
    
    def show_help(self):
        """Show help dialog"""
        help_text = """JARVIS COMMANDS:

Voice & Text Commands:
• "Hello" or "Hi" - Greet JARVIS
• "What time is it?" - Get current time
• "What is the date?" - Get current date
• "Open [app]" - Open application (notepad, calculator, browser)
• "Visit [website]" - Open a website (google, youtube, github, twitter)
• "Search [query]" - Search the web
• "Weather in [city]" - Get weather information
• "Take a screenshot" - Capture your screen

Quick Tips:
• Use the 🎤 Listen button for voice commands
• Type commands and press Enter
• Check microphone permissions if voice doesn't work
• Internet required for weather and web search
"""
        messagebox.showinfo("JARVIS Help", help_text)
    
    def clear_chat(self):
        """Clear chat history"""
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.delete(1.0, tk.END)
        self.chat_display.config(state=tk.DISABLED)
        self.add_message("Chat cleared 🗑️", "system")


def main():
    root = tk.Tk()
    app = JARVIS_UI(root)
    root.mainloop()


if __name__ == "__main__":
    main()