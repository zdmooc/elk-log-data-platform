# Stratégie Data Quality (logs)

## Dimensions
- Validité (schéma / types)
- Complétude (champs requis)
- Unicité (déduplication si besoin)
- Cohérence (valeurs attendues)
- Fraîcheur (retard ingestion)

## Implémentation
- “DQ Runner” : job périodique qui calcule des métriques DQ et indexe dans Elasticsearch
- Alerting : seuils DQ en alerte (Kibana alerting / webhook)
