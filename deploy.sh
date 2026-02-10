#!/bin/bash
cd /home/alex/docker/landing-page
git fetch origin
LOCAL=$(git rev-parse HEAD)
REMOTE=$(git rev-parse origin/main)
if [ "$LOCAL" != "$REMOTE" ]; then
  git pull origin main
  docker cp index.html nginx-proxy-manager:/var/www/html/index.html
  echo "Deployed at $(date)"
fi
