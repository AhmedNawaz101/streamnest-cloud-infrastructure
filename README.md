# StreamNest Cloud Infrastructure on Microsoft Azure

**CE 308/408 — Cloud Computing | GIKI**

## Overview
This repository contains the proof-of-concept implementation for StreamNest Analytics Cloud Infrastructure built on Microsoft Azure as part of Assignment 2.

## Architecture
The solution addresses two core problems simultaneously:
- **Microservices Deployment** using Docker + Azure Kubernetes Service (AKS)
- **Data Lakehouse Pipeline** using Azure Blob Storage + Azure Synapse Analytics

## Repository Structure
├── app.py              # Flask Content Catalog API (microservice)
├── Dockerfile          # Docker container definition
├── watch_events.csv    # Simulated StreamNest user watch events dataset
└── README.md           # This file

## Microservice — Content Catalog API
A containerized Flask API representing StreamNest's backend microservice.

### Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Service status and version |
| `/catalog` | GET | Full content catalog in JSON |

### Public Endpoint
http://57.162.161.124
http://57.162.161.124/catalog

## Data Lakehouse Pipeline
| Layer | Azure Service | Details |
|-------|--------------|---------|
| Raw Ingestion | Azure Blob Storage | watch_events.csv in raw-events container |
| Query Layer | Azure Synapse Analytics | External table dbo.watch_events |
| Analytics | Synapse SQL | Aggregated business queries |

## Dataset Fields
| Field | Description |
|-------|-------------|
| user_id | Unique user identifier |
| content_id | Content being watched |
| watch_duration | Duration in seconds |
| device_type | mobile, desktop, smart_tv, tablet |
| timestamp | Event timestamp |
| region | Geographic region |

## Azure Resources
- **Resource Group:** streamnest-rg
- **Storage Account:** sneststore2023466
- **Synapse Workspace:** streamnest-synapse
- **AKS Cluster:** streamnest-aks
- **Container Registry:** streamnestacrregistry

## Business Questions Answered
1. Which content received the most total watch time?
2. Which device type is most popular in each region?

## Technologies Used
- Microsoft Azure (AKS, Blob Storage, Synapse Analytics, ACR)
- Docker & Kubernetes
- Python (Flask)
- SQL (Synapse Serverless)
