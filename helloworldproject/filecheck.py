# import os

# print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pathlib import Path

print(Path(__file__).resolve().parent.parent)
