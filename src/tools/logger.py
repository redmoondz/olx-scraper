import pytz
import os
import logging
from datetime import datetime

from pathlib import Path
import sys
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))
from config.config import log_dir, log_level

def current_time_str():
    pytz_timezone = pytz.timezone("Europe/Kyiv")
    return datetime.now(pytz_timezone).strftime("%Y-%m-%d %H:%M")

def setup_logger():
    """Настройка логгера для записи в файл с текущей датой и временем."""
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_file = os.path.join(log_dir, f"scraper_{current_time_str()[:10].replace(' ', '_').replace(':', '-')}.log")
    

    logger = logging.getLogger("olx_scraper")
    logger.setLevel(getattr(logging, log_level.upper(), log_level))
    
    file_handler = logging.FileHandler(log_file)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    
    return logger