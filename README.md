# 🚀 Microservices DevOps Project

A fully containerized 3-tier application built with Docker and Docker Compose.

## 🏗️ Architecture

    ┌─────────────────────────────────────────┐
    │            Docker Network               │
    │                                         │
    │  ┌──────────┐  ┌──────────┐  ┌───────┐ │
    │  │ Frontend │─▶│ Backend  │─▶│  DB   │ │
    │  │  nginx   │  │  Flask   │  │Postgre│ │
    │  │ port 3000│  │ port 5000│  │  5432 │ │
    │  └──────────┘  └──────────┘  └───────┘ │
    │   (healthy)     (healthy)    (healthy)  │
    └─────────────────────────────────────────┘

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | HTML, JavaScript, nginx |
| Backend | Python, Flask, Flask-CORS |
| Database | PostgreSQL 15 |
| Containerization | Docker, Docker Compose |
| Health Monitoring | Docker Healthchecks |

## ✨ Features

- 3-tier microservices architecture
- All services containerized with Docker
- Services communicate over a private Docker network
- Health checks on all 3 services
- Data persisted using Docker volumes
- Backend waits for DB to be healthy before starting

## 🚀 How to Run

Prerequisites: Docker Desktop installed

    git clone https://github.com/DeepDhar75/microservices-devops-project.git
    cd microservices-devops-project
    docker compose up --build

Then open:
- Frontend → http://localhost:3000
- Backend API → http://localhost:5000
- Health Check → http://localhost:5000/health

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Backend status |
| GET | /health | Health check with DB status |
| GET | /notes | Get all notes |
| POST | /notes | Add a new note |

## 📁 Project Structure

    microservices-app/
    ├── frontend/
    │   ├── Dockerfile
    │   └── index.html
    ├── backend/
    │   ├── Dockerfile
    │   ├── app.py
    │   └── requirements.txt
    ├── docker-compose.yml
    └── README.md

## 🧠 Key Learnings

- How to containerize multi-service applications
- Docker networking between containers
- Service dependency management with health checks
- Data persistence using Docker volumes
- CORS configuration for cross-origin requests

## 👤 Author
Deep Dhar — DevOps Portfolio Project