"""Logging Configuration"""

import logging
from pathlib import Path

_loggers = {}

def setup_logger(log_file=None):
    """Setup logging configuration"""
    log_format = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(log_format)
    
    # File handler
    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(log_format)
    
    # Root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)
    root_logger.addHandler(console_handler)
    
    if log_file:
        root_logger.addHandler(file_handler)
    
    return root_logger

def get_logger(name):
    """Get a logger instance"""
    if name not in _loggers:
        _loggers[name] = logging.getLogger(name)
    return _loggers[name]
