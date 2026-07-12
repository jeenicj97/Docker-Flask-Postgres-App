# 📦 Flask + Postgres Dockerized Application

## 🚀 Overview
This project demonstrates how to **Dockerize a full-stack application** using:
- **Flask** as the backend framework
- **Postgres** as the database
- **Docker Compose** for orchestration

The goal was to containerize the app end-to-end, ensuring reproducibility, portability, and ease of deployment.

---
## 📌 Key Features
- Multi-stage Dockerfile for a lean, secure image
- Non-root user inside the container
- PostgreSQL with persistent volume storage
- Custom Docker network for service-to-service communication
- Health checks on the database service
- Fully configurable via `.env`
---
 
## 🏗️ Architecture
 
```
┌─────────────────┐        ┌──────────────────┐
│   Flask App      │ ─────▶ │   PostgreSQL DB   │
│   (port 5000)     │        │   (port 5432)      │
└─────────────────┘        └──────────────────┘
        │                              │
        └──────── docker-network ───────┘
                (custom bridge network)
```
 
---
 
## 📂 Project Structure
 
```
.
.
├── app/
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── .env
└── README.md
```
 
---
 
## ⚙️ Environment Variables
 
Create a `.env` file in the project root:

 ```
POSTGRES_DB=employee_db1
POSTGRES_USER=postgres1
POSTGRES_PASSWORD=password1
```
 
---
 
## 🚀 Getting Started
 
### Prerequisites
- Docker & Docker Compose installed
- Git
### 1. Clone the repo
```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
```
 
### 2. Set up environment variables
```bash
cp .env.example .env
# edit .env with your own values
```
 
### 3. Build and run with Docker Compose
```bash
docker compose up --build
```
 
The app will be available at:
```
http://localhost:5000
```
 
### 4. Stop the containers
```bash
docker compose down
```
 
To also remove the database volume (⚠️ deletes data):
```bash
docker compose down -v
```
 
---
 
## 🧪 Running from Docker Hub (No Local Build)
 
To verify the image works standalone, pulled fresh from Docker Hub:
 
```bash
docker pull jeenicj97/flask-app:v1
docker compose up
```
 
**Docker Hub Image:** https://hub.docker.com/repository/docker/jeenicj97/flask-app
 
---
 
 
## 🛠️ Challenges Faced
- Fixing Postgres readiness timing using `healthcheck` + `depends_on: condition: service_healthy`
- Reducing image size using a multi-stage build and `python:3.12-slim` base
- Ensuring the Flask container ran as a non-root user without breaking file permissions
---
 
## 📦 Image Details
 
| Detail          | Value              |
|------------------|---------------------|
| Base image        | `python:3.12-slim`   |
| Final image size  | `132 MB`            |
| User              | `appuser` |
 
---

 
