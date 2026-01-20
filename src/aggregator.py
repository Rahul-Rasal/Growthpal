import json
from collections import defaultdict

INPUT = "data/processed/structured.json"
OUTPUT = "data/aggregated/metrics.json"

with open(INPUT) as f:
    data = json.load(f)

metrics = {
    "total_records": len(data),
    "websites_with_case_study": len({
        d["website"] for d in data
        if d["section"] == "case_study" and d["content"]
    }),
    "content_length_by_section": defaultdict(list)
}

for d in data:
    metrics["content_length_by_section"][d["section"]].append(len(d["content"]))

metrics["content_length_by_section"] = {
    k: sum(v) // len(v) if v else 0
    for k, v in metrics["content_length_by_section"].items()
}

with open(OUTPUT, "w") as f:
    json.dump(metrics, f, indent=2)
