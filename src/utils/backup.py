"""Backup Utilities"""

import shutil
from pathlib import Path
from datetime import datetime
from src.utils.logger import get_logger

logger = get_logger(__name__)

class BackupManager:
    """Manages world backups"""
    
    def __init__(self, world_dir="world", backup_dir="backups"):
        self.world_dir = Path(world_dir)
        self.backup_dir = Path(backup_dir)
        self.backup_dir.mkdir(exist_ok=True)
    
    def create_backup(self, name=None):
        """Create a world backup"""
        if not self.world_dir.exists():
            logger.error(f"World directory not found: {self.world_dir}")
            return False
        
        if name is None:
            name = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        backup_path = self.backup_dir / name
        
        try:
            shutil.copytree(self.world_dir, backup_path)
            logger.info(f"Backup created: {backup_path}")
            return True
        except Exception as e:
            logger.error(f"Error creating backup: {e}")
            return False
    
    def restore_backup(self, backup_name):
        """Restore from a backup"""
        backup_path = self.backup_dir / backup_name
        
        if not backup_path.exists():
            logger.error(f"Backup not found: {backup_path}")
            return False
        
        try:
            if self.world_dir.exists():
                shutil.rmtree(self.world_dir)
            shutil.copytree(backup_path, self.world_dir)
            logger.info(f"Backup restored: {backup_name}")
            return True
        except Exception as e:
            logger.error(f"Error restoring backup: {e}")
            return False
    
    def list_backups(self):
        """List available backups"""
        return [d.name for d in self.backup_dir.iterdir() if d.is_dir()]
    
    def delete_backup(self, backup_name):
        """Delete a backup"""
        backup_path = self.backup_dir / backup_name
        
        try:
            shutil.rmtree(backup_path)
            logger.info(f"Backup deleted: {backup_name}")
            return True
        except Exception as e:
            logger.error(f"Error deleting backup: {e}")
            return False
