import argparse
import yaml
import requests
from datetime import datetime, timezone

def now_iso():
  return datetime.now(timezone.utc).isoformat()

def es_count(es, index, query):
  r = requests.get(f"{es}/{index}/_count", json=query, timeout=10)
  r.raise_for_status()
  return r.json().get("count", 0)

def main():
  ap = argparse.ArgumentParser()
  ap.add_argument("--es", default="http://localhost:9200")
  ap.add_argument("--rules", default="pipelines/quality/dq_rules.yml")
  ap.add_argument("--metrics-index", default="logs.dq.metrics")
  args = ap.parse_args()

  rules = yaml.safe_load(open(args.rules, "r", encoding="utf-8"))

  for ds in rules.get("datasets", []):
    name = ds["name"]
    idx = f"{name}-*"

    total = es_count(args.es, idx, {"query": {"match_all": {}}})
    parsefails = es_count(args.es, "logs.dq.parsefail-*", {"query": {"term": {"event.dataset.keyword": name}}})

    parsing_ok_rate = 1.0 if total == 0 else max(0.0, (total - parsefails) / total)

    doc = {
      "@timestamp": now_iso(),
      "event": {"dataset": name, "kind": "metric"},
      "dq": {
        "total_docs": total,
        "parsefails": parsefails,
        "parsing_ok_rate": parsing_ok_rate
      }
    }

    requests.post(f"{args.es}/{args.metrics_index}/_doc", json=doc, timeout=10).raise_for_status()
    print(f"[DQ] {name}: total={total} parsefails={parsefails} parsing_ok_rate={parsing_ok_rate:.4f}")

if __name__ == "__main__":
  main()
