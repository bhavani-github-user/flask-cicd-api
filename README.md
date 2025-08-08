# DevOps Project – Deployment on GCP

## 📌 Project Overview
This project demonstrates the end-to-end deployment of an application on **Google Cloud Platform (GCP)** using DevOps practices.  
It covers provisioning, deployment, and automation, ensuring scalability, monitoring, and version control integration.  

The purpose is to showcase skills in **GCP services**, **CI/CD pipelines**, and **infrastructure automation**.

---

## 🚀 Features
- Automated provisioning of infrastructure on GCP
- CI/CD pipeline for continuous integration and deployment
- Application deployment on GCP Compute Engine / GKE
- Logging and monitoring with GCP tools
- Version control integration with GitHub

---

## 🛠 Technologies Used
- **Cloud Provider:** Google Cloud Platform (GCP)
- **CI/CD Tool:** Jenkins / GitHub Actions (based on requirement)
- **Containerization:** Docker
- **Orchestration (Optional):** Kubernetes (GKE)
- **Monitoring:** GCP Monitoring / Stackdriver
- **Scripting:** Shell / Python
- **Version Control:** Git & GitHub

---

## 🏗 Architecture
1. **Code Commit** → Push code to GitHub repository
2. **CI/CD Trigger** → Jenkins or GitHub Actions starts the build process
3. **Docker Image Build** → Dockerfile builds application image
4. **Push to Container Registry** → Store image in GCP Artifact Registry
5. **Deploy to GCP** → Deploy on Compute Engine or GKE
6. **Monitoring** → GCP Monitoring collects logs and metrics

---

## 📋 Prerequisites
Before running this project, ensure you have:
- **GCP Account** with billing enabled
- **gcloud CLI** installed
- **Git** installed
- **Docker** installed
- **Jenkins** (if using CI/CD locally)
- Access to a **GitHub repository**

---

### ⚙️ Setup & Deployment for GCP DevOps Project

## 1️⃣ Clone the Repository
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>

## 2️⃣ Authenticate with GCP
gcloud auth login
gcloud config set project <your-gcp-project-id>

## 3️⃣ Build the Docker Image
docker build -t gcp-devops-app .

## 4️⃣ Run the Docker Container
docker run -d -p 8080:8080 --name myapp gcp-devops-app:latest

## 5️⃣ Access the Application in Browser
# Replace <EXTERNAL_IP> with the VM or GCP instance external IP
echo "Application running at: http://<EXTERNAL_IP>:8080"
