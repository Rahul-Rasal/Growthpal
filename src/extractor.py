from bs4 import BeautifulSoup
import os, json

RAW_DIR = "data/raw"
OUT_FILE = "data/processed/extracted.json"
os.makedirs("data/processed", exist_ok=True)

records = []

for site in os.listdir(RAW_DIR):
    path = f"{RAW_DIR}/{site}/homepage.html"
    if not os.path.exists(path):
        continue

    with open(path, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    def get_text(tag):
        return tag.get_text(separator=" ", strip=True) if tag else ""

    records.append({
        "website": f"https://{site}",
        "navbar": get_text(soup.find("nav")),
        "homepage": get_text(soup.find("main") or soup.body),
        "footer": get_text(soup.find("footer")),
        "case_study": ""  # keep empty if not found
    })

with open(OUT_FILE, "w") as f:
    json.dump(records, f, indent=2)
