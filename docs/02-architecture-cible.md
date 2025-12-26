# Architecture cible (macro)

**Collecte**
- Agents : Elastic Agent / Beats / alternatives open-source
- Normalisation : JSON, ECS

**Ingestion**
- Kafka topics par domaine (app/system/security), environnement, criticité

**Transformation**
- Logstash : parsing + enrichment + routage
- Flink (option) : agrégations/anomalies/corrélations

**Stockage**
- Elasticsearch : data streams, index templates, ILM, tiers

**Restitution**
- Kibana : dashboards / alerting / investigations
- Grafana (option) : vues SRE / exec

**Qualité**
- contrôles DQ et métriques DQ (index dédiés)
