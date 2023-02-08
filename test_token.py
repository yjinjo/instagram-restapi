from pathlib import Path
from dotenv import load_dotenv
import os
import requests

load_dotenv()

TOKEN = os.environ.get("SIMPLE_JWT_TOKEN")

headers = {
    "Authorization": f"Bearer {TOKEN}",
}

res = requests.get("http://localhost:8000/post/1/", headers=headers)
print(res.json())
