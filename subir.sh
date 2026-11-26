#!/bin/bash
# Sube un archivo a un sitio del hosting compartido de Hostinger (cuenta u806273835).
# Uso: HOSTINGER_API_TOKEN=xxxx ./subir.sh crmformeta.com publicado/kommo-crm/index.html kommo-crm/index.html
# El token NO va en el repo: pedirlo a Miguel (está en el gestor de contraseñas).
set -e
: "${HOSTINGER_API_TOKEN:?Falta HOSTINGER_API_TOKEN}"
DOM=$1; F=$2; R=$3; SIZE=$(wc -c < "$F" | tr -d ' ')
J=$(curl -s -X POST -H "Authorization: Bearer $HOSTINGER_API_TOKEN" -H 'Content-Type: application/json' \
  -d "{\"username\":\"u806273835\",\"domain\":\"$DOM\"}" https://developers.hostinger.com/api/hosting/v1/files/upload-urls)
get(){ echo "$J" | python3 -c "import json,sys;print(json.load(sys.stdin)['$1'])"; }
URL=$(get url); A=$(get auth_key); AR=$(get rest_auth_key)
curl -s -o /dev/null -w "crear %{http_code}\n" -X POST "$URL/$R?override=true" -H "X-Auth: $A" -H "X-Auth-Rest: $AR" \
  -H "Tus-Resumable: 1.0.0" -H "Upload-Length: $SIZE" -H "Upload-Offset: 0"
curl -s -o /dev/null -w "subir %{http_code}\n" -X PATCH "$URL/$R?override=true" -H "X-Auth: $A" -H "X-Auth-Rest: $AR" \
  -H "Tus-Resumable: 1.0.0" -H "Content-Type: application/offset+octet-stream" -H "Upload-Offset: 0" --data-binary "@$F"
