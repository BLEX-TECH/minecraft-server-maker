"""Dashboard Panel for Server Monitoring"""

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QGroupBox,
    QLabel, QProgressBar, QTextEdit, QScrollArea
)
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QFont, QColor

from src.utils.logger import get_logger

logger = get_logger(__name__)

class DashboardPanel(QWidget):
    """Dashboard for monitoring server statistics"""
    
    def __init__(self, server_manager):
        super().__init__()
        self.server_manager = server_manager
        self.setup_ui()
    
    def setup_ui(self):
        """Setup dashboard UI"""
        layout = QVBoxLayout(self)
        layout.setSpacing(10)
        layout.setContentsMargins(10, 10, 10, 10)
        
        # Server Status Group
        status_group = QGroupBox("Server Status")
        status_layout = QHBoxLayout()
        
        self.status_label = QLabel("Status: Offline")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.status_label.setFont(font)
        status_layout.addWidget(self.status_label)
        
        self.uptime_label = QLabel("Uptime: 0h 0m 0s")
        status_layout.addWidget(self.uptime_label)
        
        status_layout.addStretch()
        status_group.setLayout(status_layout)
        layout.addWidget(status_group)
        
        # Performance Group
        perf_group = QGroupBox("Performance")
        perf_layout = QVBoxLayout()
        
        # CPU Usage
        cpu_layout = QHBoxLayout()
        cpu_label = QLabel("CPU Usage:")
        cpu_layout.addWidget(cpu_label)
        self.cpu_bar = QProgressBar()
        self.cpu_bar.setMaximum(100)
        cpu_layout.addWidget(self.cpu_bar)
        self.cpu_text = QLabel("0%")
        cpu_layout.addWidget(self.cpu_text)
        perf_layout.addLayout(cpu_layout)
        
        # Memory Usage
        mem_layout = QHBoxLayout()
        mem_label = QLabel("Memory Usage:")
        mem_layout.addWidget(mem_label)
        self.mem_bar = QProgressBar()
        self.mem_bar.setMaximum(100)
        mem_layout.addWidget(self.mem_bar)
        self.mem_text = QLabel("0 MB")
        mem_layout.addWidget(self.mem_text)
        perf_layout.addLayout(mem_layout)
        
        perf_group.setLayout(perf_layout)
        layout.addWidget(perf_group)
        
        # Server Info Group
        info_group = QGroupBox("Server Information")
        info_layout = QVBoxLayout()
        
        self.info_labels = {}
        for key in ["Address", "Port", "Version", "Players", "TPS"]:
            h_layout = QHBoxLayout()
            label = QLabel(f"{key}:")
            label.setMinimumWidth(100)
            value = QLabel("N/A")
            self.info_labels[key] = value
            h_layout.addWidget(label)
            h_layout.addWidget(value)
            h_layout.addStretch()
            info_layout.addLayout(h_layout)
        
        info_group.setLayout(info_layout)
        layout.addWidget(info_group)
        
        # Recent Logs
        logs_group = QGroupBox("Recent Logs")
        logs_layout = QVBoxLayout()
        
        self.logs_text = QTextEdit()
        self.logs_text.setReadOnly(True)
        self.logs_text.setMaximumHeight(200)
        self.logs_text.setFontFamily("Courier New")
        self.logs_text.setFontPointSize(9)
        logs_layout.addWidget(self.logs_text)
        
        logs_group.setLayout(logs_layout)
        layout.addWidget(logs_group)
        
        layout.addStretch()
    
    def refresh_stats(self):
        """Refresh statistics display"""
        stats = self.server_manager.get_stats()
        
        if self.server_manager.is_running():
            self.status_label.setText("Status: ✓ Online")
            self.status_label.setStyleSheet("color: #00ff00;")
        else:
            self.status_label.setText("Status: ✗ Offline")
            self.status_label.setStyleSheet("color: #ff0000;")
        
        # Update CPU and Memory
        cpu = stats.get("cpu", 0)
        self.cpu_bar.setValue(int(cpu))
        self.cpu_text.setText(f"{cpu:.1f}%")
        
        mem = stats.get("memory", 0)
        self.mem_bar.setValue(int(min(mem / 1024, 100)))  # Convert to percentage
        self.mem_text.setText(f"{mem:.0f} MB")
        
        # Update server info
        self.info_labels["Port"].setText(str(stats.get("port", 25565)))
        self.info_labels["Players"].setText(f"{stats.get('players', 0)}/{stats.get('max_players', 20)}")
        self.info_labels["TPS"].setText(f"{stats.get('tps', 20.0):.1f}")
        
        # Update logs
        logs = self.server_manager.get_recent_logs(5)
        self.logs_text.setPlainText("\n".join(logs))
        # Auto-scroll to bottom
        self.logs_text.verticalScrollBar().setValue(
            self.logs_text.verticalScrollBar().maximum()
        )
