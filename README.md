# Log Data Platform — Observabilité orientée usages (ELK + Kafka)

Ce dépôt est un **projet "prêt à cadrer"** pour un Grand-Compte visant la **refonte de l’offre logs** (applicatifs, systèmes, réseau, sécurité) avec une approche **data & métiers** (et non “infra-only”).

## Objectifs
- Industrialiser la chaîne **collecte → transformation → stockage → restitution**.
- Passer à une offre **standardisée, gouvernée, exploitable** (qualité, traçabilité, contrats).
- Supporter **forte volumétrie** et usages **batch + temps réel** (Kafka).
- Accélérer la mise à disposition de **cas d’usage observabilité** (Ops / SecOps / Métiers).

## Architecture cible (log-centric / data-centric)
1. **Agents** (Elastic Agent / Beats / alternatives) collectent des logs et métriques.
2. **Kafka** centralise et découple l’ingestion (topics par domaine / criticité / tenant).
3. **Processing** :
   - **Logstash** (parsing, enrichment, routing) pour la majorité des flux.
   - **Flink** (optionnel) pour agrégations temps réel, détection d’anomalies, corrélations.
4. **Elasticsearch** : stockage, recherche, analytics, indexation ECS.
5. **Kibana** (et extension Grafana possible) : dashboards, alerting, exploration.
6. **Data Quality & Governance** : contrats, contrôles, monitoring DQ, runbooks.

## Quickstart local (dév)
Pré-requis : Docker + Docker Compose.

```bash
cd local
docker compose up -d
```

Générer des logs et les pousser dans Kafka :
```bash
python -m venv .venv && . .venv/bin/activate
pip install -r pipelines/requirements.txt
python pipelines/generators/log_generator.py --bootstrap localhost:9092 --topic logs.app.demo
```

## Livrables clés
- **Contrats de données logs** (ECS + conventions), templates d’index, ILM, mapping.
- **Pipelines d’ingestion** (Logstash) + exemples de jobs (Flink skeleton).
- **Contrôles qualité** (schéma, complétude, duplication, fraîcheur, seuils).
- **Dashboards Kibana** (exports NDJSON) + principes de dataviz.
- **CI/CD** (lint/test/build + packaging + déploiement) et runbooks d’exploitation.

## Structure du repo
Voir l’arborescence ci-dessous.


## Arborescence
```text
.
├─ docs/
│  ├─ 00-vision-produit.md
│  ├─ 01-cadrage-kpis-usages.md
│  ├─ 02-architecture-cible.md
│  ├─ 03-contrats-et-ecs.md
│  ├─ 04-strategie-dq.md
│  ├─ 05-runbooks.md
│  └─ adr/
│     ├─ 0001-ecs-as-default.md
│     ├─ 0002-kafka-as-ingestion-bus.md
│     └─ 0003-ilm-and-data-tiers.md
├─ pipelines/
│  ├─ logstash/
│  │  ├─ pipelines.yml
│  │  ├─ conf.d/
│  │  │  ├─ 10-input-kafka.conf
│  │  │  ├─ 20-parse-enrich.conf
│  │  │  └─ 90-output-elasticsearch.conf
│  │  └─ patterns/
│  │     └─ custom.grok
│  ├─ flink/
│  │  └─ skeleton-java/
│  │     ├─ README.md
│  │     └─ src/main/java/com/acme/logs/FlinkJob.java
│  ├─ quality/
│  │  ├─ dq_rules.yml
│  │  ├─ dq_runner.py
│  │  └─ README.md
│  ├─ generators/
│  │  └─ log_generator.py
│  └─ requirements.txt
├─ elastic/
│  ├─ index-templates/
│  │  ├─ logs-app-template.json
│  │  ├─ logs-system-template.json
│  │  └─ logs-security-template.json
│  ├─ ilm/
│  │  └─ ilm-hot-warm-cold.json
│  └─ kibana/
│     └─ dashboards/
│        └─ demo-observability.ndjson
├─ ci/
│  ├─ github-actions/
│  │  └─ ci.yml
│  └─ gitlab/
│     └─ .gitlab-ci.yml
├─ local/
│  ├─ docker-compose.yml
│  └─ README.md
├─ scripts/
│  ├─ bootstrap-topics.sh
│  ├─ apply-elastic-assets.sh
│  └─ smoke-tests.sh
├─ Makefile
├─ .editorconfig
├─ .gitignore
└─ LICENSE

```
