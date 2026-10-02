#!/bin/bash
clear
echo "=== STARTING WORKSPACE SETUP==="
echo "Creating project folders"
mkdir -p project/src project/logs project/config
echo "Initializing config file"
touch project/config/settings.conf
echo "DB_HOST=localhost" >> project/config/settings.conf
echo "Workspace structure created successfully:"
ls -R project
echo "=== SETUP COMPLETE ===" 