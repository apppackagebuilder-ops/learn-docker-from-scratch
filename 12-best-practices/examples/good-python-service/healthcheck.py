import sys
from urllib.request import urlopen

try:
    with urlopen('http://127.0.0.1:8000/health', timeout=3) as response:
        if response.status == 200:
            sys.exit(0)
except Exception:
    pass

sys.exit(1)
