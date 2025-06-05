
#  Neo4j - FastAPI Project  
**Author: Ilias BENLARBI**

---

##  FastAPI

This project uses FastAPI to create two RESTful API endpoints that interact with a remote Neo4j database.

###  How to Run the Application

```bash
uvicorn main:app --reload
```

📄 API Documentation: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### 📡 Available Endpoints

- **POST** `/employee` – Create an employee  
  Request body:
  ```json
  {
    "name": "string",
    "emp_id": 0
  }
  ```

- **GET** `/employees` – Retrieve all employees

---

##  Docker

Docker is used to containerize the FastAPI application and host it on DockerHub.

###  Commands

```bash
# Authenticate with DockerHub
docker login

# Build the Docker image
docker build -t neo4jfastapi .

# Run the container locally
docker run -it --rm -p 8000:8000 neo4jfastapi

# Tag the image for DockerHub
docker tag neo4jfastapi:latest lneb/neo4jfastapi

# Push the image to DockerHub
docker push lneb/neo4jfastapi:latest
```

---

##  AWS Deployment

AWS is used to deploy and host the FastAPI container.

###  IAM (Identity and Access Management)

- Create a user with permissions for **ECR** and **ECS**
- Generate access credentials (Access Key ID and Secret Access Key)

###  ECR (Elastic Container Registry)

- Create a Docker image repository to store container images

###  ECS (Elastic Container Service)

- Create a **cluster**
- Define a **task definition**
- Create a **service**
- Configure an IAM **role**
- Ensure **port 8000** is open in the security group for external access

---

##  GitHub Actions – CI/CD

This project uses GitHub Actions to automate the CI/CD pipeline and AWS deployment.

There are two workflows:

- **CI/CD Workflow** (`ci-cd.yaml`)  
  Builds and pushes the Docker image to DockerHub.

- **AWS Deployment Workflow** (`aws.yaml`)  
  Pulls the latest Docker image and deploys it to ECS.

###  Required GitHub Secrets

- `AWS_USER`, `AWS_PWD`
- `DOCKER_USER`, `DOCKER_PWD`, `REPO_NAME`

---

###  CI/CD Workflow Details (`.github/workflows/ci-cd.yaml`)

Triggered on every `git push`.

#### Jobs:

- **CI**:
  - Set up a Linux environment
  - Install Python and dependencies
  - Format code with `black`
  - Lint code for errors

- **CD**:
  - Login to DockerHub
  - Build Docker image with timestamp
  - Push image to DockerHub

---

###  AWS Deployment Workflow Details (`.github/workflows/aws.yaml`)

Also triggered on `git push`.

Steps include:

- Login to AWS using GitHub Secrets
- Pull latest Docker image from DockerHub
- Build, tag, and push image to ECR
- Update ECS task definition with new image ID
- Deploy updated task to ECS cluster

---

##  Summary

This project demonstrates a full deployment workflow from development to production using:

- **FastAPI** for backend API
- **Neo4j** for the graph database
- **Docker** for containerization
- **AWS (ECR & ECS)** for cloud deployment
- **GitHub Actions** for CI/CD automation
