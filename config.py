"""
Configurações gerais do projeto:
Statistics for Data Science with Python — IBM
"""

from pathlib import Path

# Diretório raiz do projeto
BASE_DIR = Path(__file__).resolve().parent

# Estruturas principais
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

NOTEBOOKS_DIR = BASE_DIR / "notebooks"
DOCS_DIR = BASE_DIR / "docs"
SCRIPTS_DIR = BASE_DIR / "scripts"
OUTPUTS_DIR = BASE_DIR / "outputs"
FIGURES_DIR = OUTPUTS_DIR / "figures"
REPORTS_DIR = OUTPUTS_DIR / "reports"
MODELS_DIR = BASE_DIR / "models"

def show_paths():
    """Exibe os caminhos principais do projeto."""
    print("BASE_DIR:", BASE_DIR)
    print("RAW_DATA_DIR:", RAW_DATA_DIR)
    print("PROCESSED_DATA_DIR:", PROCESSED_DATA_DIR)
    print("NOTEBOOKS_DIR:", NOTEBOOKS_DIR)
    print("DOCS_DIR:", DOCS_DIR)
    print("OUTPUTS_DIR:", OUTPUTS_DIR)
    print("MODELS_DIR:", MODELS_DIR)
