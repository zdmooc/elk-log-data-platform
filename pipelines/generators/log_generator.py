import argparse
import json
import time
import uuid
from datetime import datetime, timezone

from kafka import KafkaProducer

def now_iso():
  return datetime.now(timezone.utc).isoformat()

def main():
  ap = argparse.ArgumentParser()
  ap.add_argument("--bootstrap", default="localhost:9092")
  ap.add_argument("--topic", default="logs.app.demo")
  ap.add_argument("--rate", type=float, default=5.0, help="events/sec")
  args = ap.parse_args()

  producer = KafkaProducer(
    bootstrap_servers=args.bootstrap,
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
  )

  sleep_s = 1.0 / max(args.rate, 0.1)
  i = 0
  while True:
    evt = {
      "@timestamp": now_iso(),
      "message": f"demo log event {i}",
      "log": {"level": "INFO"},
      "event": {"dataset": args.topic, "kind": "event"},
      "service": {"name": "demo-app", "environment": "dev"},
      "trace": {"id": uuid.uuid4().hex},
      "labels": {"team": "platform-observability"},
    }
    producer.send(args.topic, evt)
    i += 1
    time.sleep(sleep_s)

if __name__ == "__main__":
  main()
