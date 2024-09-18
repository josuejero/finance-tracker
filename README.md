# Finance Tracker Application

## Overview

**Finance Tracker** is a web application designed to help users manage their personal finances by tracking payments, debts, balances, and transactions. Built with **Django**, the application allows users to easily input financial information, predict potential shortfalls, and calculate projected balances over time. The project also includes **Celery** for background task processing, and it's containerized for easy deployment via **Docker** and **Kubernetes**.

## Features

- **Track Payments, Debts, and Balances**: Record and manage recurring payments, debts, and account balances.
- **Balance Projection**: Calculate projected balances based on income, expenses, and future payments.
- **Shortfall Prediction**: Predict when a user's balance will fall short based on upcoming expenses.
- **Celery Background Tasks**: Automatically update balances in the background using Celery.
- **Scalable Deployment**: Easily deploy the application with Docker and Kubernetes, including horizontal scaling via Kubernetes Horizontal Pod Autoscaler (HPA).

## Technology Stack

- **Backend**: Python, Django, Celery
- **Frontend**: Django Templates
- **Database**: SQLite (for development), PostgreSQL (recommended for production)
- **Task Processing**: Celery with Redis as the message broker
- **Containerization**: Docker, Kubernetes
- **CI/CD**: Jenkins pipeline for continuous integration and deployment
- **Secret Management**: Google Cloud Secret Manager for securely storing credentials

## Prerequisites

To run the project locally, you'll need:

- **Python 3.9+**
- **Docker** (for containerized deployment)
- **Kubernetes CLI** (`kubectl`) and a Kubernetes cluster (for production deployments)
- **Redis** (for Celery task queue)
- **PostgreSQL** (recommended for production environments)
- **Jenkins** (for CI/CD pipeline)
- **Google Cloud Account** (for secret management and deployment to GCP)

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/josuejero/finance-tracker.git
cd finance-tracker
```

### 2. Set Up a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root and add the following:

```bash
SECRET_KEY=your-django-secret-key
DATABASE_URL=your-database-url
OAUTH_CLIENT_ID=your-google-oauth-client-id
OAUTH_CLIENT_SECRET=your-google-oauth-client-secret
REDIS_URL=your-redis-url
ENCRYPTION_KEY=your-encryption-key
```

### 5. Apply Migrations

```bash
python manage.py migrate
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

### 7. Running Celery for Background Tasks

Start the Celery worker:

```bash
celery -A finance_tracker_django worker --loglevel=info
```

### 8. Running Redis (for Celery)

Make sure Redis is running on your local machine or via Docker:

```bash
docker run -d -p 6379:6379 redis
```

## Docker Setup

### 1. Build the Docker Image

```bash
docker build -t finance-tracker .
```

### 2. Run the Docker Container

```bash
docker run -p 8000:8000 --env-file .env finance-tracker
```

## Kubernetes Setup

### 1. Deploy to Kubernetes

To deploy to a Kubernetes cluster, ensure you have `kubectl` configured for your cluster and apply the Kubernetes manifests:

```bash
kubectl apply -f k8s/
```

### 2. Horizontal Pod Autoscaling

The application is configured to scale horizontally using Kubernetes HPA. Ensure metrics server is installed on your cluster and apply the HPA configuration:

```bash
kubectl apply -f k8s/hpa.yaml
```

## Continuous Integration and Deployment (CI/CD)

A **Jenkinsfile** is included for CI/CD. Configure Jenkins with appropriate credentials (e.g., `GOOGLE_PROJECT_ID`, `OAUTH_CLIENT_ID`, and `OAUTH_CLIENT_SECRET`) to automate the following stages:

- **Build**: Builds the Docker image.
- **Test**: Runs the Django tests.
- **Deploy**: Deploys the application to a Kubernetes cluster.

## Running Tests

To run the tests locally:

```bash
python manage.py test
```

Or, using Docker:

```bash
docker-compose run web python manage.py test
```

## Security

This project uses **Google Cloud Secret Manager** to securely handle sensitive credentials such as OAuth tokens and the database URL. Ensure that the necessary secrets are created in Google Cloud and available to the application.

## Contributing

Contributions are welcome! Please fork this repository, make your changes, and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).