# Azure CLI commands used with this project

# Creating Python environment

python3 -m venv ~/.myrepo
source ~/.myrepo/bin/activate

# Install, lint, and test the application

make all

# Deploy a webapp application

az webapp up -n azure-pipeline-ws-sjg

# See that the webapp is running

az webapp list --output table

# Request housing price prediction

./make_predict_azure_app.sh

# Stream log file

 az webapp log tail

