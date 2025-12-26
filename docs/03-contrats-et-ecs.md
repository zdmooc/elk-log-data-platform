# Contrats de données & ECS

## Pourquoi ECS ?
- Standardisation transverse
- Réutilisabilité des dashboards/alertes
- Facilite la gouvernance (champs obligatoires / optionnels)

## Conventions (extrait)
- Champs “minimum viable” :
  - @timestamp, event.dataset, log.level, message
  - service.name, service.environment
  - host.name, agent.type
- Dataset : event.dataset = logs.<domaine>.<application>
- Versioning : event.module + tags + mapping versionné
