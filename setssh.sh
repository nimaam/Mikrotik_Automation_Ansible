#!/bin/bash

# MikroTik RouterOS API URL
API_URL="http://192.168.12.254:8728/rest"
# Replace 'mikrotik_ip' with your MikroTik's IP address

# Credentials
USERNAME="admin"
PASSWORD="Sunny.8949"
# Replace 'admin' and 'password' with your actual username and password

# SSH Settings
# This is where you'd define the SSH settings. Note that this format is hypothetical
# and must be adapted to your actual API's requirements.
SSH_SETTINGS='{
  "strong-crypto": "yes",
  "host-key-size": 2048,
  "forwarding-enabled": "both"
}'

# Example curl command to modify settings (this is a placeholder and likely needs to be adjusted)
curl -u "$USERNAME:$PASSWORD" -X POST -H "Content-Type: application/json" \
     -d "$SSH_SETTINGS" "$API_URL/path/to/ssh/settings"

