docker exec -i $1 /bin/bash -c "export OAUTH_CALLBACK_URL=$2 && jupyterhub -f /configs/jupyterhub_config_ultraauth.py"

