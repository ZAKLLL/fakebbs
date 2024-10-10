# FastAPI Web Application

This project is a web application built with FastAPI, featuring a user interface powered by Amis and containerized using Docker.

## Features

- FastAPI backend
- Amis-powered frontend
- Docker containerization
- GitHub Actions for CI/CD
- Nacos service registration

## Project Structure

The main components of the project are:

- `main.py`: The entry point of the FastAPI application
- `webUI/`: Contains the frontend-related files
- `api/`: Contains API route definitions
- `config/`: Configuration files, including Swagger and Nacos setup
- `Dockerfile`: Defines the Docker image for the application
- `.github/workflows/deploy.yml`: GitHub Actions workflow for deployment

## Setup and Installation

1. Clone the repository
2. Install dependencies:
   ```pip install -r requirements.txt```
3. Run the application:
   ```uvicorn main:app --reload```

## Docker Deployment

To build and run the Docker container:

1. Build the Docker image:
   ```docker build -t your-fastapi-app .```
2. Run the container:
   ```docker run -d -p 8000:80 your-fastapi-app```

## CI/CD

This project uses GitHub Actions for continuous integration and deployment. The workflow is defined in:

