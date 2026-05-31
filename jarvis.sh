#!/bin/bash
# JARVIS-XXXIX Launcher for macOS/Linux
# Automatically installs dependencies and starts JARVIS

echo ""
echo "========================================"
echo "🤖 JARVIS-XXXIX - Advanced AI Assistant"
echo "========================================"
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 not found."
    echo "Install from: https://www.python.org"
    exit 1
fi

# Check Python version
PYTHON_VERSION=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
echo "✅ Python $PYTHON_VERSION detected"

# Run setup
echo ""
echo "Running setup..."
python3 setup.py

# Run main
echo ""
echo "Launching JARVIS-XXXIX..."
python3 main.py