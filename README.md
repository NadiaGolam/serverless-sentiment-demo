# Serverless Sentiment Analysis Demo (Dockerized)

## Description
# Serverless Text Sentiment Analysis Service

A serverless, cloud-native system for analyzing sentiment in uploaded text files using AWS services. This repository includes a containerized demo using Flask that mimics the cloud sentiment pipeline.

## 🌐 Overview

This project demonstrates:
- Serverless design patterns
- Event-driven architecture using AWS Lambda
- Sentiment analysis via AWS Comprehend
- NoSQL storage using DynamoDB
- CI/CD pipeline with GitHub Actions
- Docker-based demo environment for local simulation

---

## 🧱 Technologies Used

| Service       | Purpose                     |
|---------------|-----------------------------|
| AWS S3        | File storage/input          |
| AWS Lambda    | Event-driven processing     |
| AWS Comprehend| Sentiment analysis          |
| DynamoDB      | Sentiment result storage    |
| Flask         | Local simulation app        |
| Docker        | Containerization            |
| GitHub Actions| CI/CD for lint/testing      |

---

## 🚀 Run the Docker Demo Locally

### Prerequisites
- [Docker installed](https://docs.docker.com/get-docker/)

### Steps

```bash
# Clone the repo
git clone https://github.com/NadiaGolam/serverless-sentiment-demo.git
cd serverless-sentiment-demo

# Build Docker image
docker build -t sentiment-demo .

# Run the app
docker run -p 5000:5000 sentiment-demo


## How to Use

### Build the Docker Image
```bash
docker build -t sentiment-demo .
```

### Run the Container
```bash
docker run -p 5000:5000 sentiment-demo
```

### Test with CURL or Postman
```bash
curl -X POST http://localhost:5000/analyze -H "Content-Type: application/json" -d '{"text":"I love cloud computing"}'

```

Expected output:
```json
{
  "text": "I love cloud computing",
  "sentiment": "Positive"
}

```
