# **Finance App on Google Cloud Platform**

Microservice architecture: streamlit as frontend, flask/fastapi as backend.

## Tech: 
- Cloud Run: running docker container applications, 
- BigQuery: data warehouse
- Cloud Build & Google Container Registry: managing continous deployment
- streamlit: python framework for building data apps
- fastapi/flask: backend framework to manage api calls realted to data management

## Repo Set-up
Warning: Althoug it is advised to keep separate repos for multiple microservices - in order to maintain simplicity, I store all the code in one repository. Also note that this repo is connected to Cloud Resource Repositories so the files can be accesed on GCP.