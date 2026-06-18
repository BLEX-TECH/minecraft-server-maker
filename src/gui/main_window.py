"""Main Window for Minecraft Server Maker"""

from PyQt6.QtWidgets import (
    QMainWindow, QVBoxLayout, QHBoxLayout, QWidget,
    QTabWidget, QPushButton, QLabel, QStatusBar
)
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QFont, QIcon

from src.gui.styles import DARK_THEME
from src.gui.dashboard import DashboardPanel
from src.gui.settings_panel import SettingsPanel
from src.server.server_manager import ServerManager
from src.utils.logger import get_logger

logger = get_logger(__name__)

class MainWindow(QMainWindow):
    """Main application window"""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Minecraft Server Maker")
        self.setGeometry(100, 100, 1200, 800)
        
        # Initialize server manager
        self.server_manager = ServerManager()
        
        # Setup UI
        self.setup_ui()
        
        # Apply stylesheet
        self.setStyleSheet(DARK_THEME)
        
        # Setup update timer
        self.update_timer = QTimer()
        self.update_timer.timeout.connect(self.update_status)
        self.update_timer.start(1000)  # Update every second
        
        logger.info("Main window initialized")
    
    def setup_ui(self):
        """Setup the user interface"""
        # Create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Create main layout
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(10)
        
        # Create tab widget
        self.tabs = QTabWidget()
        
        # Create dashboard panel
        self.dashboard = DashboardPanel(self.server_manager)
        self.tabs.addTab(self.dashboard, "Dashboard")
        
        # Create settings panel
        self.settings = SettingsPanel(self.server_manager)
        self.tabs.addTab(self.settings, "Settings")
        
        main_layout.addWidget(self.tabs)
        
        # Create control buttons
        button_layout = QHBoxLayout()
        
        self.start_btn = QPushButton("Start Server")
        self.start_btn.clicked.connect(self.start_server)
        self.start_btn.setMinimumHeight(40)
        button_layout.addWidget(self.start_btn)
        
        self.stop_btn = QPushButton("Stop Server")
        self.stop_btn.clicked.connect(self.stop_server)
        self.stop_btn.setMinimumHeight(40)
        self.stop_btn.setEnabled(False)
        button_layout.addWidget(self.stop_btn)
        
        self.restart_btn = QPushButton("Restart Server")
        self.restart_btn.clicked.connect(self.restart_server)
        self.restart_btn.setMinimumHeight(40)
        self.restart_btn.setEnabled(False)
        button_layout.addWidget(self.restart_btn)
        
        main_layout.addLayout(button_layout)
        
        # Create status bar
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.status_label = QLabel("Server: Stopped")
        self.statusBar.addWidget(self.status_label)
        
        # Add player count label
        self.player_label = QLabel("Players: 0/20")
        self.statusBar.addPermanentWidget(self.player_label)
    
    def start_server(self):
        """Start the Minecraft server"""
        logger.info("Start button clicked")
        self.server_manager.start()
        self.update_button_states()
        self.statusBar.showMessage("Server starting...", 3000)
    
    def stop_server(self):
        """Stop the Minecraft server"""
        logger.info("Stop button clicked")
        self.server_manager.stop()
        self.update_button_states()
        self.statusBar.showMessage("Server stopped", 3000)
    
    def restart_server(self):
        """Restart the Minecraft server"""
        logger.info("Restart button clicked")
        self.server_manager.restart()
        self.update_button_states()
        self.statusBar.showMessage("Server restarting...", 3000)
    
    def update_button_states(self):
        """Update button enabled/disabled states"""
        is_running = self.server_manager.is_running()
        self.start_btn.setEnabled(not is_running)
        self.stop_btn.setEnabled(is_running)
        self.restart_btn.setEnabled(is_running)
    
    def update_status(self):
        """Update status information"""
        is_running = self.server_manager.is_running()
        
        if is_running:
            self.status_label.setText("Server: ✓ Running")
            stats = self.server_manager.get_stats()
            player_count = stats.get("players", 0)
            max_players = stats.get("max_players", 20)
            self.player_label.setText(f"Players: {player_count}/{max_players}")
        else:
            self.status_label.setText("Server: ✗ Stopped")
            self.player_label.setText("Players: 0/20")
        
        self.update_button_states()
        self.dashboard.refresh_stats()
