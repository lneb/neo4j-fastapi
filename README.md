Neo4j - FastAPI Project / Ilias BENLARBI

---------------------------------
FastAPI

FastAPI creates 2 API to communicate with a distant Neo4j database

How to run : uvicorn main:app --reload     
http://127.0.0.1:8000/docs


- POST /employee CREATE EMPLOYEE
{
  "name": "string",
  "emp_id": 0
}

- GET /employees Get All Employees


---------------------------------
Docker

Docker is used to create images of FastAPI and host it on DockerHub

Commands : 
docker login
docker build -t neo4jfastapi .
docker run -it --rm -p 8000:8000 neo4jfastapi
docker tag neo4jfastapi:latest lneb/neo4jfastapi
docker push lneb/neo4jfastapi:latest

---------------------------------
AWS

AWS is used to host FASTAPI Solution 


IAM :
Create a user with the right credentials (ECR & ECS)
Generate an access key (3rd party key)

ECR: 
Create a referential

ECS:
Create a cluster
Create a task
Create a role
(make sure the right port is open in order to run FastAPI)
---------------------------------
Git

Git is used to run pipelines with actions.
CICD yaml is used to generate a Docker image from main.py and to send it to DockerHub
AWS yaml is used to link the lastest docker image and deploy it via ECS.

When a git push is made, CICD and after AWS start.


Secrets :
- AWS USER,PWD
- DOCKER USER,PWD, REPO NAME


Actions : 


CI-CD YAML
	- Activation on git push
	- jobs : 
		CI : 
			- install linux
			- install python and dependencies
			- check code with black and lint
		CD : 
			- Docker login
			- Docker build with timestamp
			- Docker push

AWS YAML 
	- Activation on git push
	- AWS Login (AWS Key_ID, Secret_Key and region)
	- Build, tag, and push image from DockerHub to Amazon ECR
	- Download the task definition
	- Link the image ID to the task
	- Deploy to ECS