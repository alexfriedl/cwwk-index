#!/bin/sh
cd /home/alex/docker/landing-page
git fetch origin
git reset --hard origin/main
echo "Deployed at $(date)" >> deploy.log
