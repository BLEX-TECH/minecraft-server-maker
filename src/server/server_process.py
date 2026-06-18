"""Server Process - Manages the actual Minecraft server process"""

import subprocess
import sys
from pathlib import Path
from src.utils.logger import get_logger

logger = get_logger(__name__)

class ServerProcess:
    """Manages Minecraft server subprocess"""
    
    def __init__(self, config):
        self.config = config
        self.process = None
        self.jar_path = Path("server/server.jar")
    
    def start(self):
        """Start the server process"""
        if not self.jar_path.exists():
            logger.error(f"Server JAR not found at {self.jar_path}")
            return False
        
        try:
            ram_gb = self.config.get("ram_gb", 2)
            args = [
                sys.executable,
                "-Xmx" + str(ram_gb) + "G",
                "-Xms" + str(ram_gb) + "G",
                "-jar",
                str(self.jar_path),
                "nogui"
            ]
            
            self.process = subprocess.Popen(
                args,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            logger.info("Server process started")
            return True
        except Exception as e:
            logger.error(f"Error starting server: {e}")
            return False
    
    def stop(self):
        """Stop the server process"""
        if self.process:
            try:
                self.process.terminate()
                self.process.wait(timeout=10)
                logger.info("Server process stopped")
            except subprocess.TimeoutExpired:
                self.process.kill()
                logger.warning("Server process killed")
            finally:
                self.process = None
    
    def is_running(self):
        """Check if process is running"""
        return self.process is not None and self.process.poll() is None
