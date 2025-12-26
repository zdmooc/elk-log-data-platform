# Vision produit (offre logs orientée usages)

## Problème
L’offre logs historique est souvent **hétérogène**, difficile à exploiter, et centrée sur l’outillage plutôt que sur la valeur.

## Proposition
Une offre groupe “Log Data Platform” structurée comme un produit :
- **Data contracts** (ECS + conventions + versioning)
- **Pipelines industrialisés** (Kafka → Logstash/Flink → Elasticsearch)
- **Qualité & fiabilité** (contrôles DQ + SLO + alerting)
- **Self-service** (catalogue de datasets logs, dashboards “prêts à l’emploi”)
- **Multi-tenant** (domaines, environnements, RBAC, rétention)

## Principes
- “**Logs as Data**”: tout log est une donnée gouvernée.
- “**Standard first**”: ECS + templates d’index + ILM.
- “**Shift-left observability**”: conventions côté applicatifs.
- “**Automate everything**”: CI/CD, tests, provisioning d’assets.
