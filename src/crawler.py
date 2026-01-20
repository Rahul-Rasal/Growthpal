import requests, os, json
from datetime import datetime

WEBSITES = [
    "https://www.godaddy.com",
    "https://stripe.com",
    "https://shopify.com",
    "https://digitalocean.com",
    "https://hashicorp.com"
]

RAW_DIR = "data/raw"
os.makedirs(RAW_DIR, exist_ok=True)

def crawl():
    for url in WEBSITES:
        domain = url.replace("https://", "").replace("/", "")
        site_dir = f"{RAW_DIR}/{domain}"
        os.makedirs(site_dir, exist_ok=True)

        response = requests.get(url, timeout=10)

        with open(f"{site_dir}/homepage.html", "w", encoding="utf-8") as f:
            f.write(response.text)

        metadata = {
            "url": url,
            "status_code": response.status_code,
            "crawl_time": datetime.utcnow().isoformat()
        }

        with open(f"{site_dir}/metadata.json", "w") as f:
            json.dump(metadata, f, indent=2)

if __name__ == "__main__":
    crawl()
