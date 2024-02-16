import os
try:
    import requests
except ImportError:
    os.system("pip install requests")
    import requests


def short(link: str):
    ...