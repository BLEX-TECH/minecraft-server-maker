"""Settings Panel for Server Configuration"""

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QGroupBox,
    QLabel, QLineEdit, QSpinBox, QComboBox,
    QPushButton, QCheckBox, QScrollArea, QMessageBox
)
from PyQt6.QtCore import Qt

from src.utils.logger import get_logger

logger = get_logger(__name__)

class SettingsPanel(QWidget):
    """Settings configuration panel"""
    
    def __init__(self, server_manager):
        super().__init__()
        self.server_manager = server_manager
        self.setup_ui()
        self.load_settings()
    
    def setup_ui(self):
        """Setup settings UI"""
        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(10)
        main_layout.setContentsMargins(10, 10, 10, 10)
        
        # Scroll area for settings
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout(scroll_widget)
        
        # Basic Settings Group
        basic_group = QGroupBox("Basic Settings")
        basic_layout = QVBoxLayout()
        
        # Server Name
        name_layout = QHBoxLayout()
        name_layout.addWidget(QLabel("Server Name:"))
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("My Minecraft Server")
        name_layout.addWidget(self.name_input)
        basic_layout.addLayout(name_layout)
        
        # Server Description
        desc_layout = QHBoxLayout()
        desc_layout.addWidget(QLabel("Description:"))
        self.desc_input = QLineEdit()
        self.desc_input.setPlaceholderText("A fun place to play!")
        desc_layout.addWidget(self.desc_input)
        basic_layout.addLayout(desc_layout)
        
        basic_group.setLayout(basic_layout)
        scroll_layout.addWidget(basic_group)
        
        # Network Settings Group
        network_group = QGroupBox("Network Settings")
        network_layout = QVBoxLayout()
        
        # Port
        port_layout = QHBoxLayout()
        port_layout.addWidget(QLabel("Port:"))
        self.port_spin = QSpinBox()
        self.port_spin.setMinimum(1024)
        self.port_spin.setMaximum(65535)
        self.port_spin.setValue(25565)
        port_layout.addWidget(self.port_spin)
        port_layout.addStretch()
        network_layout.addLayout(port_layout)
        
        # Max Players
        players_layout = QHBoxLayout()
        players_layout.addWidget(QLabel("Max Players:"))
        self.max_players_spin = QSpinBox()
        self.max_players_spin.setMinimum(1)
        self.max_players_spin.setMaximum(100)
        self.max_players_spin.setValue(20)
        players_layout.addWidget(self.max_players_spin)
        players_layout.addStretch()
        network_layout.addLayout(players_layout)
        
        network_group.setLayout(network_layout)
        scroll_layout.addWidget(network_group)
        
        # Game Settings Group
        game_group = QGroupBox("Game Settings")
        game_layout = QVBoxLayout()
        
        # Game Mode
        mode_layout = QHBoxLayout()
        mode_layout.addWidget(QLabel("Game Mode:"))
        self.gamemode_combo = QComboBox()
        self.gamemode_combo.addItems(["Survival", "Creative", "Adventure", "Spectator"])
        mode_layout.addWidget(self.gamemode_combo)
        mode_layout.addStretch()
        game_layout.addLayout(mode_layout)
        
        # Difficulty
        diff_layout = QHBoxLayout()
        diff_layout.addWidget(QLabel("Difficulty:"))
        self.difficulty_combo = QComboBox()
        self.difficulty_combo.addItems(["Peaceful", "Easy", "Normal", "Hard"])
        self.difficulty_combo.setCurrentText("Normal")
        diff_layout.addWidget(self.difficulty_combo)
        diff_layout.addStretch()
        game_layout.addLayout(diff_layout)
        
        # PvP
        self.pvp_check = QCheckBox("Enable PvP")
        self.pvp_check.setChecked(True)
        game_layout.addWidget(self.pvp_check)
        
        # Spawn Protection
        spawn_layout = QHBoxLayout()
        spawn_layout.addWidget(QLabel("Spawn Protection Radius:"))
        self.spawn_spin = QSpinBox()
        self.spawn_spin.setMinimum(0)
        self.spawn_spin.setMaximum(100)
        self.spawn_spin.setValue(16)
        spawn_layout.addWidget(self.spawn_spin)
        spawn_layout.addStretch()
        game_layout.addLayout(spawn_layout)
        
        game_group.setLayout(game_layout)
        scroll_layout.addWidget(game_group)
        
        # Performance Settings Group
        perf_group = QGroupBox("Performance Settings")
        perf_layout = QVBoxLayout()
        
        # RAM Allocation
        ram_layout = QHBoxLayout()
        ram_layout.addWidget(QLabel("RAM Allocation (GB):"))
        self.ram_spin = QSpinBox()
        self.ram_spin.setMinimum(1)
        self.ram_spin.setMaximum(64)
        self.ram_spin.setValue(2)
        ram_layout.addWidget(self.ram_spin)
        ram_layout.addStretch()
        perf_layout.addLayout(ram_layout)
        
        # View Distance
        view_layout = QHBoxLayout()
        view_layout.addWidget(QLabel("View Distance (chunks):"))
        self.view_spin = QSpinBox()
        self.view_spin.setMinimum(3)
        self.view_spin.setMaximum(32)
        self.view_spin.setValue(10)
        view_layout.addWidget(self.view_spin)
        view_layout.addStretch()
        perf_layout.addLayout(view_layout)
        
        perf_group.setLayout(perf_layout)
        scroll_layout.addWidget(perf_group)
        
        scroll_layout.addStretch()
        scroll.setWidget(scroll_widget)
        main_layout.addWidget(scroll)
        
        # Save/Reset buttons
        button_layout = QHBoxLayout()
        
        self.save_btn = QPushButton("Save Settings")
        self.save_btn.clicked.connect(self.save_settings)
        self.save_btn.setMinimumHeight(40)
        button_layout.addWidget(self.save_btn)
        
        self.reset_btn = QPushButton("Reset to Defaults")
        self.reset_btn.clicked.connect(self.reset_settings)
        self.reset_btn.setMinimumHeight(40)
        button_layout.addWidget(self.reset_btn)
        
        main_layout.addLayout(button_layout)
    
    def load_settings(self):
        """Load settings from server manager"""
        config = self.server_manager.get_config()
        
        self.name_input.setText(config.get("server_name", "My Minecraft Server"))
        self.desc_input.setText(config.get("description", ""))
        self.port_spin.setValue(config.get("port", 25565))
        self.max_players_spin.setValue(config.get("max_players", 20))
        self.gamemode_combo.setCurrentText(config.get("gamemode", "Survival"))
        self.difficulty_combo.setCurrentText(config.get("difficulty", "Normal"))
        self.pvp_check.setChecked(config.get("pvp", True))
        self.spawn_spin.setValue(config.get("spawn_protection", 16))
        self.ram_spin.setValue(config.get("ram_gb", 2))
        self.view_spin.setValue(config.get("view_distance", 10))
    
    def save_settings(self):
        """Save settings to server manager"""
        config = {
            "server_name": self.name_input.text(),
            "description": self.desc_input.text(),
            "port": self.port_spin.value(),
            "max_players": self.max_players_spin.value(),
            "gamemode": self.gamemode_combo.currentText(),
            "difficulty": self.difficulty_combo.currentText(),
            "pvp": self.pvp_check.isChecked(),
            "spawn_protection": self.spawn_spin.value(),
            "ram_gb": self.ram_spin.value(),
            "view_distance": self.view_spin.value(),
        }
        
        self.server_manager.save_config(config)
        logger.info("Settings saved")
        
        QMessageBox.information(self, "Success", "Settings saved successfully!")
    
    def reset_settings(self):
        """Reset settings to defaults"""
        reply = QMessageBox.question(self, "Confirm", "Reset all settings to defaults?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if reply == QMessageBox.StandardButton.Yes:
            self.server_manager.reset_config()
            self.load_settings()
            logger.info("Settings reset to defaults")
