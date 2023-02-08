from pathlib import Path
from dotenv import load_dotenv
import os
import requests

load_dotenv()

TOKEN = os.environ.get("TOKEN")

headers = {
    "Authorization": f"Token {TOKEN}",
}

res = requests.get("http://localhost:8000/post/1/", headers=headers)
print(res.json())
