export CELLXGENE_LOCATION=`which cellxgene`
export CELLXGENE_DATA=/mnt/data/sc
export GATEWAY_IP=35.205.85.182
export USER_FILE="users.json"

#Once these are set, you run like a normal Flask app
cellxgene-gateway
