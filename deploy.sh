#!/bin/sh
cd /home/alex/docker/landing-page
git fetch origin
git pull origin main
docker cp index.html nginx-proxy-manager:/var/www/html/index.html
echo "Deployed at $(date)"
