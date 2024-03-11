# k8sisfun Project

Welcome to the k8sisfun project! This repository is part of a larger project.

## Repositories

- [API Service Repository](https://github.com/Nivrin/k8sIsFun-APIService)
- [Data Service Repository](https://github.com/Nivrin/k8sIsFun-DataService)
- [Simple Front Repository](https://github.com/Nivrin/k8sIsFun-SimpleFront)

# API Service Documentation

Welcome to the documentation for my API service, which provides endpoints for retrieving state codes and names.

## Overview

The API service is a Flask application that serves as an intermediary between clients and the data service. It exposes two endpoints: one for retrieving state codes based on a given state name and another for retrieving state names based on a given state code.

## Endpoints

- **GET /codetostate**: Retrieves the state name corresponding to a given state code.
- **GET /statetocode**: Retrieves the state code corresponding to a given state name.

## Usage

To use the API service, send HTTP requests to the appropriate endpoint:

- **GET /codetostate**: Provide a state code as a query parameter named `code`.
  Example: `curl http://<api_service_url>/codetostate?code=NY`
- **GET /statetocode**: Provide a state name as a query parameter named `state`.
  Example: `curl http://<api_service_url>/statetocode?state=New York`

## Installation and Setup

To deploy the API service, follow these steps:

1. Clone the repository:

    ```bash
    git clone <repository_url>
    ```

2. Navigate to the project directory:

    ```bash
    cd <project_directory>
    ```

3. Build the Docker image:

    ```bash
    docker build -t api-service .
    ```

## Deployment

To deploy the API service on Kubernetes, use the provided deployment and service YAML files:

1. Apply the Kubernetes service configuration:

    ```bash
    kubectl apply -f manifests/api_service-service.yaml
    ```

2. Apply the Kubernetes deployment configuration:

    ```bash
    kubectl apply -f manifests/api_service-deployment.yaml
    ```

## Continuous Integration/Continuous Deployment (CI/CD)

We use GitHub Actions for CI/CD. The workflow defined in the `google.yaml` file automates the building, publishing, and deploying processes.
