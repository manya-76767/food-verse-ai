
import sys
from pathlib import Path

backend_path = Path(__file__).parent / "artifacts" / "food-verse-ai" / "backend"
sys.path.insert(0, str(backend_path))

from app import app
