$(aws ecr get-login --no-include-email --region us-east-1)
docker build -t myjupyterhub .
docker tag myjupyterhub:latest 557345145383.dkr.ecr.us-east-1.amazonaws.com/jupyterhub:latest
docker push 557345145383.dkr.ecr.us-east-1.amazonaws.com/jupyterhub:latest
aws ecs update-service --cluster JupyterHub --service JupyterHubDemo2 --task-definition JupyterHubDemo --force-new-deployment
