# paths.py
from pathlib import Path

# Project Root
PROJECT_ROOT = Path().resolve().parent.parent

# environment variables
ENV_PATH = PROJECT_ROOT / ".env"

# Directories paths
BASE_DIR = PROJECT_ROOT / "analisis_datos"
DATA_DIR = BASE_DIR / "data"
NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"
UTILS_DIR = PROJECT_ROOT / "utils"
REFERENCES_DIR = PROJECT_ROOT / "references"

# Data Directories
DATA_RAW_DIR = DATA_DIR / "raw"
DATA_PROCESSED_DIR = DATA_DIR / "processed"
