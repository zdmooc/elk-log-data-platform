.PHONY: help lint test up down bootstrap apply-assets smoke

help:
	@echo "Targets:"
	@echo "  up            - Start local stack (Kafka + ES + Kibana + Logstash)"
	@echo "  down          - Stop local stack"
	@echo "  bootstrap     - Create Kafka topics"
	@echo "  apply-assets  - Apply ES templates + ILM + Kibana demo assets"
	@echo "  smoke         - Run smoke tests"
	@echo "  lint/test     - Run basic checks"

up:
	cd local && docker compose up -d

down:
	cd local && docker compose down -v

bootstrap:
	bash scripts/bootstrap-topics.sh

apply-assets:
	bash scripts/apply-elastic-assets.sh

smoke:
	bash scripts/smoke-tests.sh

lint:
	python -m compileall pipelines

test:
	python -m unittest discover -s pipelines -p "test_*.py" || true
