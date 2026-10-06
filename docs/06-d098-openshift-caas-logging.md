# D-098 — OpenShift CaaS Logging / Incident Correlation Integration

**Status:** ARCHITECTURE_READY / LIVE OPENSHIFT EVIDENCE PENDING

## Purpose

Provide the logging contribution to the SQY Expert Kubernetes/OpenShift mission without turning this
specialist log platform into the universal owner of all observability.

## Mission role

The CaaS operations stack must be able to correlate:

- platform alert;
- Kubernetes/OpenShift event;
- workload log;
- GitOps state;
- identity/policy failure;
- incident timeline.

## Target integration

~~~text
OpenShift / Kubernetes
  pods / nodes / operators / ingress / policies
              |
              v
       log collector
              |
              v
      Kafka optional
              |
              v
 Logstash / pipeline
              |
              v
 Elasticsearch / OpenSearch
              |
              v
 Kibana / search / alert context
              |
              +--------+
              |        |
              v        v
         Prometheus   N3/RCA
         Alertmanager incident record
~~~

Kafka is optional for the SQY runtime proof. The core requirement is searchable logs plus correlation,
not re-deploying the full log-data architecture on the workstation.

## Minimum SQY-5 proof

A disposable incident should demonstrate:

1. failure injected in a test workload;
2. platform/application signal visible in metrics or events;
3. relevant log located in the logging backend;
4. timestamp/correlation used to link alert/event/log;
5. recovery performed;
6. evidence captured.

Preferred bounded failures:
- readiness/probe failure;
- denied network flow;
- authentication failure;
- policy admission denial.

## Data hygiene

Do not ingest:
- real customer data;
- secrets/tokens;
- unredacted authentication headers;
- private infrastructure identifiers beyond what is needed for the local lab.

## Ownership

- metrics/tracing contracts: Shared Platform / product owners;
- cluster health: Cluster Factory;
- log-platform patterns: this repository;
- incident RCA: operating team / D-098 runbook.

## Gate contribution

This document prepares the logging slice of:
`CAAS_SECOPS_OBSERVABILITY_PACK_READY`.

A design document is not a live logging proof.
