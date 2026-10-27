
import os
import sys

sys.path.insert(
    0,
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "artifacts",
        "food-verse-ai",
        "backend",
    ),
)

from app import app
