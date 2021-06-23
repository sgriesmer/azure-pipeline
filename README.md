# Overview

The purpose of this project is to create a Continuous Integration/Continuous Delivery (CI/CD) pipeline for a Python Machine Learning Flask application.  The application returns a prediction of a median housing price of a house in the Boston area given a set of input variables.

## Project Plan
The project plan for the pipeline is described in a Trello board and spreadsheet:

Trello Board: https://urldefense.com/v3/__https://trello.com/b/fPufDYN5/azure-pipeline__;!!BhdT!1tKzq60elvX4JeWiTR_IXuGxxPS_GZg2Vrom05KtOiEh6-HJkbvgRfM7$

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

![build and deploy from Azure DevOps](/images/pipeline-build-and-destroy-from-azure-devops.png)

In Github, you should see a screen like this for build job:

![build job from git hub](/images/build-job-from-github.png)

(11) Test the successful deployment of the application by requesting a predication of a median housing price

Execute the command:

    ./make_predict_azure_app.sh

You should see the output:

![prediction from web app](/images/prediction-from-web-app.png)

(12) The output of the tailed log file should look like:

![tailed log file](/images/tailed-log-file.png)

(13) Running a load test using locust with 1 test client with 3 users generated the following output:

![locust testing](/images/locust-testing.png)

![locust chart](/images/locust-chart.png)


## Enhancements

<TODO: A short description of how to improve the project in the future>

## Demo 

<TODO: Add link Screencast on YouTube>



