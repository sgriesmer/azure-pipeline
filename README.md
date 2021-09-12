# DevOps Engineer for Microsoft Azure Nanodegree Program

## Project: Building a CI/CD pipeline

## Overview

The purpose of this project is to create a Continuous Integration/Continuous Delivery (CI/CD) pipeline for a Python Machine Learning Flask application.  The application returns a prediction of a median housing price of a house in the Boston area given a set of input variables.

## Project Plan
The project plan for the pipeline is described in a Trello board and spreadsheet:

Trello Board: https://na01.safelinks.protection.outlook.com/?url=https%3A%2F%2Ftrello.com%2Fb%2FfPufDYN5%2Fazure-pipeline&data=04%7C01%7C%7C1d781d84f0fe4e75696108d93912b205%7C84df9e7fe9f640afb435aaaaaaaaaaaa%7C1%7C0%7C637603574718249973%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C1000&sdata=H4Hph4JJcDXtRJ2Uv4tCXe%2Bds1%2BDiMtHqxOKEeM6PA0%3D&reserved=0

Spreadsheet: ![Project Management spreadsheet](project-management-template-sjg.xlsx)

## Instructions

The CI/CD pipeline consists of two separate pieces: (1) A CI pipeline implemented using Github as a repository, Azure Cloud Shell as a workspace or jump server, and Github Actions Container as a SaaS build server; and (2) A CD pipeline that uses Github as a repository and Azure Pipelines as a deployment server, deploying the application as an Azure Web App.

![CI/CD Pipeline Architecture](/images/arch.jpg)

The steps for running the CI/CD pipeline to build and deploy the application are:

(1) Fork the Github repository for the project 

Navigate to the repository github.com/sgriesmer/azure-pipeline.git.
Specify the name and choose the project where you want the fork created.
Choose Fork to create the fork.

(2) Create (or log into your Azure account)

(3) Start the Azure Cloud Shell as a workspace

(4) Clone the project from Github on Azure Cloud Shell

Create a working directory.

Execute the command:

    git clone <your repo>

![Starter Files from git clone](/images/starter-files-from-git-clone.png)

(5) Create a Python virtual environment on Azure Cloud Shell

Type the following commands into the shell:

    python3 -m venv ~/.myrepo
    source ~/.myrepo/bin/activate

(6) Install, lint, and test the application locally on Azure Cloud Shell

Execute the command:

    make all

to install, lint, and test the application into the Github repository.

Any code changes should pass tests.  The output of a successful test run should look like:

![Test results after make all](/images/test-results-after-make-all.png)

(7) Start webapp to test remotely

Execute the command:

    az webapp up -n azure-pipeline-ws-sjg

You should see the project running on the app service through the Azure Portal:

![web app in azure portal](/images/azure-pipeline-ws-in-azure-portal.png)

(8) Test the successful deployment of the application by requesting a predication of a median housing price

Execute the command:

    ./make_predict_azure_app.sh

You should see the output:

![prediction from web app](/images/prediction-from-web-app.png)

(9) Set up a pipeline with Azure Pipelines to deploy the application

    Select New Pipeline
    Select GitHub
    Select Github Repository with code
    Select Python to Linux Web App on Azure
    Select Azure subscription
    Authenticate with Azure


(10) Upload application to Github repository to trigger a build remotely as well as a deployment through Azure Pipelines

Make small non-impacting change to app.py file (e.g., add spaces to header)

    git add app.py
    git commit -m "cosmetic change to app.py to test build"
    git push

In Azure Pipelines, you should see a screen like:

![build and deploy from Azure DevOps](/images/successful-pipeline-run-in-Azure-Pipelines-with-url.png)

In Github, you should see a screen like this for build job:

![build job from git hub](/images/build-job-from-github.png)

The Github Actions badge should show that the build job passed its tests:

[![Actions Status](https://github.com/sgriesmer/azure-pipeline/workflows/Python%20application%20test%20with%20Github%20Actions/badge.svg)](https://github.com/sgriesmer/azure-pipeline/actions)

In Azure Portal, you should see the web app deployed:

![running app in Azure Portal ](/images/running-web-app-in-azure-portal.png)

In Azure Pipelines, you should also see that the application deployed:

![deployment in Azure Pipelines](/images/screen-shot-deployment-ap.png)

(11) Test the successful deployment of the application by requesting a predication of a median housing price

Execute the command:

    ./make_predict_azure_app.sh

You should see the output:

![prediction from web app](/images/prediction-from-web-app.png)

(12) The output of the tailed log file should look like:

![tailed log file](/images/tailed-log-file.png)

(13) Running a load test using locust with 1 test client with 3 users generated the following output:

(a) Load test of get function for the application:

![locust get testing](/images/locust-get-load-test.png)

(b) Load test of post /predict function for the application:

![locust post testing](/images/locust-post-predict-load-test.png)


## Enhancements

This project could be enhanced in the following ways:

(1) Use Azure Pipelines for the build and deployment rather than both Github Actions and Azure Pipelines.  It would make it simpler and easier to maintain.
(2) Link in a Jupyter notebook for the Boston Housing ML model as another pipeline, deploying the joblib or a pickle file to Github and then doing the application build and deploy.

## Demo 

Demo: https://youtu.be/ie-ZZSrkgEE



