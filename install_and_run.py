#!/usr/bin/env python3
"""
JARVIS - One-Click Installer and Runner
This script installs all dependencies and launches JARVIS
"""

import subprocess
import sys
import os

def install_dependencies():
    """Install all required dependencies"""
    print("=" * 60)
    print("JARVIS - Installing Dependencies")
    print("=" * 60)
    
    packages = [
        'pyttsx3',
        'SpeechRecognition',
        'Pillow',
        'requests'
    ]
    
    # Install PyAudio separately with special handling
    print("\n📦 Installing base packages...")
    for package in packages:
        print(f"Installing {package}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", package])
    
    # Install PyAudio with platform-specific handling
    print("\n🔧 Installing audio support (PyAudio)...")
    if sys.platform == 'win32':
        print("Windows detected - Using pipwin for PyAudio...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "pipwin"])
        subprocess.check_call(["pipwin", "install", "pyaudio"])
    else:
        print("Installing PyAudio via pip...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "pyaudio"])
    
    print("\n✅ All dependencies installed successfully!")

def run_jarvis():
    """Run JARVIS application"""
    print("\n" + "=" * 60)
    print("JARVIS - Launching Application")
    print("=" * 60 + "\n")
    
    # Import and run JARVIS
    from jarvis_main import main
    main()

if __name__ == "__main__":
    try:
        # Check if dependencies are already installed
        import pyttsx3
        import speech_recognition
        import PIL
        import requests
        print("✅ All dependencies already installed!")
    except ImportError:
        print("📥 Some dependencies are missing. Installing...\n")
        install_dependencies()
    
    # Run JARVIS
    run_jarvis()