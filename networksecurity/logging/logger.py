import logging
import os
from datetime import datetime

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

LOG_DIR = os.path.join(PROJECT_ROOT, "logs")

os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE_NAME = f"networksecurity_{datetime.now().strftime('%Y-%m-%d_%H-%M')}.log"

LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE_NAME)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger("networksecurity")