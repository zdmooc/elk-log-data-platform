# Cadrage : usages & KPI

## Usages prioritaires (exemples)
- Ops : erreurs 5xx, latence, saturation pool, timeouts
- SecOps : authent/autorisation, anomalies, détections simples
- Réseau : logs FW/proxy/DNS, corrélations
- Métiers : parcours, incidents impactants, événements clés

## KPI / SLO data
- Fraîcheur : p95 < 60s (temps réel), p95 < 15min (batch)
- Perte : < 0.1% par pipeline
- Qualité : taux de parsing OK > 99%
- Exploitabilité : champs ECS requis présents > 98%
