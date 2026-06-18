"""System Monitoring Utilities"""

import psutil
from src.utils.logger import get_logger

logger = get_logger(__name__)

class SystemMonitor:
    """Monitors system resources"""
    
    @staticmethod
    def get_cpu_usage():
        """Get current CPU usage percentage"""
        return psutil.cpu_percent(interval=0.1)
    
    @staticmethod
    def get_memory_info():
        """Get memory usage information"""
        memory = psutil.virtual_memory()
        return {
            "total": memory.total / 1024 / 1024 / 1024,  # GB
            "used": memory.used / 1024 / 1024 / 1024,  # GB
            "available": memory.available / 1024 / 1024 / 1024,  # GB
            "percent": memory.percent,
        }
    
    @staticmethod
    def get_disk_info(path="/"):
        """Get disk usage information"""
        disk = psutil.disk_usage(path)
        return {
            "total": disk.total / 1024 / 1024 / 1024,  # GB
            "used": disk.used / 1024 / 1024 / 1024,  # GB
            "free": disk.free / 1024 / 1024 / 1024,  # GB
            "percent": disk.percent,
        }
    
    @staticmethod
    def get_process_info(pid):
        """Get process resource usage"""
        try:
            process = psutil.Process(pid)
            return {
                "name": process.name(),
                "cpu_percent": process.cpu_percent(interval=0.1),
                "memory_mb": process.memory_info().rss / 1024 / 1024,
                "num_threads": process.num_threads(),
            }
        except psutil.NoSuchProcess:
            logger.error(f"Process {pid} not found")
            return None
