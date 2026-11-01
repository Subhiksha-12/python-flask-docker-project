# Python Flask Application Using Docker

## Project Description
This project demonstrates how to Dockerize a Python Flask web application using Docker.

The application runs inside a Docker container and displays a simple welcome message in the web browser.

## Technologies Used
- Python 3.11
- Flask 3.0.2
- Docker
- Git
- GitHub

## Project Structure

```text
python-docker-app/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
└── .gitignore
```

## Prerequisites
- Python (optional for local execution)
- Docker Desktop
- Git
- GitHub account

## How to Run the Application

### Step 1: Clone the Repository

```bash
git clone https://github.com/Subhiksha-12/python-flask-docker-project.git
```

### Step 2: Navigate to the Project

```bash
cd python-flask-docker-project
```

### Step 3: Build the Docker Image

```bash
docker build -t my-python-app:v1 .
```

### Step 4: Run the Docker Container

```bash
docker run -d -p 5000:5000 --name my-running-python-app my-python-app:v1
```

### Step 5: Access the Application

Open your browser and visit:

http://localhost:5000

## Docker Management Commands

Check running containers:

```bash
docker ps
```

View application logs:

```bash
docker logs my-running-python-app
```

Stop the container:

```bash
docker stop my-running-python-app
```

Start the container:

```bash
docker start my-running-python-app
```

Remove the container:

```bash
docker rm -f my-running-python-app
```

## Expected Output

Python Flask Application in Docker!

Your Python web app is running smoothly inside a Docker container.

## Author
Subhiksha-12

## Conclusion
This project demonstrates how to package and run a Python Flask application inside a Docker container, making the application easier to deploy and manage.
