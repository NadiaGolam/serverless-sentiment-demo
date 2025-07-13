# Serverless Sentiment Analysis Demo (Dockerized)

## Description
This is a Flask-based mockup to demonstrate the sentiment analysis functionality of the serverless pipeline project.

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
curl -X POST http://localhost:5000/analyze -H "Content-Type: application/json" -d '{"text":"I feel good today!"}'
```

Expected output:
```json
{"text": "I feel good today!", "sentiment": "Positive"}
```
