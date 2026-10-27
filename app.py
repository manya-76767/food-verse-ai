
import importlib.util
from pathlib import Path
import sys

backend_file = (
    Path(__file__).parent
    / "artifacts"
    / "food-verse-ai"
    / "backend"
    / "app.py"
)

spec = importlib.util.spec_from_file_location(
    "food_verse_backend", backend_file
)
backend = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = backend
spec.loader.exec_module(backend)

app = backend.app
