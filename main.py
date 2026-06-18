#!/usr/bin/env python3
"""
Minecraft Server Maker - Main Entry Point
A GUI-based tool for hosting Minecraft servers
"""

import sys
import logging
from pathlib import Path

try:
    from PyQt6.QtWidgets import QApplication
except ImportError:
    print("PyQt6 is not installed. Please run: pip install -r requirements.txt")
    sys.exit(1)

from src.gui.main_window import MainWindow
from src.utils.logger import setup_logger

# Setup logging
log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)
logger = setup_logger(log_dir / "app.log")

def main():
    """Main application entry point"""
    logger.info("Starting Minecraft Server Maker...")
    
    app = QApplication(sys.argv)
    app.setApplicationName("Minecraft Server Maker")
    app.setApplicationVersion("1.0.0")
    
    # Create and show main window
    window = MainWindow()
    window.show()
    
    logger.info("GUI loaded successfully")
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
