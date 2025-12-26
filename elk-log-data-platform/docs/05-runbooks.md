# Runbooks (extraits)

## Incident : explosion du lag Kafka
1) vérifier consommation Logstash/Flink
2) vérifier partitions & consumer group
3) activer backpressure / augmenter parallélisme
4) vérifier que les mappings ES ne provoquent pas de rejets

## Incident : parsing en échec
1) regarder tags "_grokparsefailure"
2) identifier la source / version applicative
3) mettre à jour pattern / pipeline versionné
