import json
from datetime import datetime

INPUT = "data/processed/extracted.json"
OUTPUT = "data/processed/structured.json"

with open(INPUT) as f:
    data = json.load(f)

final = []

for site in data:
    for section in ["navbar", "homepage", "footer", "case_study"]:
        final.append({
            "website": site["website"],
            "section": section,
            "content": site[section],
            "crawl_timestamp": datetime.utcnow().isoformat(),
            "isActive": True if site[section] else False
        })

with open(OUTPUT, "w") as f:
    json.dump(final, f, indent=2)
