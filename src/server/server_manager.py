"""Server Manager - Handles server lifecycle and configuration"""

import json
import psutil
from pathlib import Path
from src.utils.logger import get_logger

logger = get_logger(__name__)

class ServerManager:
    """Manages Minecraft server operations"""
    
    def __init__(self):
        self.config_file = Path("config.json")
        self.config = self.load_config()
        self.process = None
        self.logs = []
    
    def load_config(self):
        """Load configuration from file"""
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r') as f:
                    return json.load(f)
            except Exception as e:
                logger.error(f"Error loading config: {e}")
        
        return self.get_default_config()
    
    def get_default_config(self):
        """Get default configuration"""
        return {
            "server_name": "My Minecraft Server",
            "description": "A fun place to play!",
            "port": 25565,
            "max_players": 20,
            "gamemode": "Survival",
            "difficulty": "Normal",
            "pvp": True,
            "spawn_protection": 16,
            "ram_gb": 2,
            "view_distance": 10,
        }
    
    def get_config(self):
        """Get current configuration"""
        return self.config.copy()
    
    def save_config(self, config):
        """Save configuration to file"""
        try:
            self.config = config
            with open(self.config_file, 'w') as f:
                json.dump(config, f, indent=2)
            logger.info("Configuration saved")
        except Exception as e:
            logger.error(f"Error saving config: {e}")
    
    def reset_config(self):
        """Reset configuration to defaults"""
        self.config = self.get_default_config()
        self.save_config(self.config)
    
    def start(self):
        """Start the server"""
        logger.info("Starting server...")
        # Implementation for starting server process
        pass
    
    def stop(self):
        """Stop the server"""
        logger.info("Stopping server...")
        # Implementation for stopping server process
        pass
    
    def restart(self):
        """Restart the server"""
        logger.info("Restarting server...")
        self.stop()
        self.start()
    
    def is_running(self):
        """Check if server is running"""
        return self.process is not None and self.process.poll() is None
    
    def get_stats(self):
        """Get server statistics"""
        stats = {
            "cpu": 0,
            "memory": 0,
            "port": self.config.get("port", 25565),
            "players": 0,
            "max_players": self.config.get("max_players", 20),
            "tps": 20.0,
        }
        
        if self.is_running() and self.process:
            try:
                proc = psutil.Process(self.process.pid)
                stats["cpu"] = proc.cpu_percent(interval=0.1)
                stats["memory"] = proc.memory_info().rss / 1024 / 1024  # Convert to MB
            except Exception as e:
                logger.error(f"Error getting process stats: {e}")
        
        return stats
    
    def get_recent_logs(self, lines=10):
        """Get recent server logs"""
        return self.logs[-lines:] if self.logs else ["No logs available"]
    
    def add_log(self, message):
        """Add a log message"""
        self.logs.append(message)
        if len(self.logs) > 100:
            self.logs = self.logs[-100:]
