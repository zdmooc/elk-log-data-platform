# Data Quality (DQ)

Objectif: fournir des métriques DQ exploitables (par dataset, par période) :
- parsing_ok_rate
- required_fields_rate
- ingestion_latency_sec (p95)
- duplicates_rate (optionnel)

Implémentation: un script Python qui interroge Elasticsearch et indexe des métriques dans `logs.dq.metrics-*`.
