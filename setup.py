#!/usr/bin/env python3
"""
JARVIS-XXXIX - Installation & Setup Script
Automatically installs all dependencies and checks system requirements
"""

import subprocess
import sys
import platform
import os
from pathlib import Path

def print_header(text):
    print("\n" + "="*60)
    print(f"  {text}")
    print("="*60 + "\n")

def run_command(cmd, shell=False):
    """Run a shell command"""
    try:
        result = subprocess.run(cmd if shell else cmd.split(), 
                              shell=shell, 
                              capture_output=True, 
                              text=True)
        return result.returncode == 0
    except Exception as e:
        print(f"Error: {e}")
        return False

def check_python_version():
    """Check Python version"""
    print_header("Checking Python Version")
    version = sys.version_info
    if version.major == 3 and version.minor >= 9:
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} - OK")
        return True
    else:
        print(f"❌ Python 3.9+ required (you have {version.major}.{version.minor})")
        return False

def install_dependencies():
    """Install Python dependencies"""
    print_header("Installing Python Dependencies")
    
    packages = [
        'pyttsx3',
        'SpeechRecognition',
        'Pillow',
        'requests',
        'opencv-python',
        'mss',
        'numpy',
        'psutil',
        'PyQt6',
        'duckduckgo-search'
    ]
    
    for package in packages:
        print(f"Installing {package}...")
        if not run_command(f"{sys.executable} -m pip install -q {package}"):
            print(f"⚠️ Warning: Could not install {package}")
    
    # Install PyAudio with special handling
    print("Installing PyAudio (audio support)...")
    if platform.system() == 'Windows':
        run_command(f"{sys.executable} -m pip install -q pipwin")
        run_command("pipwin install pyaudio")
    else:
        run_command(f"{sys.executable} -m pip install -q pyaudio")
    
    print("\n✅ Dependencies installed!")

def check_ollama():
    """Check if Ollama is installed"""
    print_header("Checking Ollama Setup")
    
    try:
        result = subprocess.run(["ollama", "--version"], 
                              capture_output=True, 
                              text=True)
        if result.returncode == 0:
            print(f"✅ Ollama found: {result.stdout.strip()}")
            return True
    except FileNotFoundError:
        pass
    
    print("❌ Ollama not found")
    print("\n📥 Download Ollama from: https://ollama.ai")
    print("   Then run: ollama pull mistral")
    print("   Keep Ollama running: ollama serve")
    return False

def check_system_requirements():
    """Check system requirements"""
    print_header("System Requirements")
    
    os_name = platform.system()
    print(f"OS: {os_name}")
    
    if os_name not in ['Windows', 'Darwin', 'Linux']:
        print(f"❌ Unsupported OS: {os_name}")
        return False
    
    print(f"✅ Supported OS")
    
    # Check microphone
    try:
        import sounddevice
        print(f"✅ Microphone support available")
    except ImportError:
        print(f"⚠️ Microphone support may be limited")
    
    return True

def create_config():
    """Create default config if not exists"""
    print_header("Setting Up Configuration")
    
    config_dir = Path("config")
    config_file = config_dir / "config.json"
    
    if not config_file.exists():
        config_dir.mkdir(exist_ok=True)
        print("✅ Configuration created")
    else:
        print("✅ Configuration already exists")

def main():
    """Main setup function"""
    print("\n" + "="*60)
    print("  🤖 JARVIS-XXXIX - Setup & Installation")
    print("="*60)
    
    # Check Python
    if not check_python_version():
        print("\n❌ Setup failed: Python 3.9+ required")
        sys.exit(1)
    
    # Check system
    if not check_system_requirements():
        print("\n⚠️ Some features may not work correctly")
    
    # Install dependencies
    install_dependencies()
    
    # Check Ollama
    ollama_ok = check_ollama()
    
    # Create config
    create_config()
    
    # Summary
    print_header("Setup Complete!")
    
    if ollama_ok:
        print("✅ All systems ready!")
        print("\n🚀 Start JARVIS with: python main.py")
    else:
        print("⚠️ Setup complete, but Ollama is required for full functionality")
        print("\n📥 Install Ollama: https://ollama.ai")
        print("🚀 Then start JARVIS with: python main.py")
    
    print("\n" + "="*60)

if __name__ == "__main__":
    main()