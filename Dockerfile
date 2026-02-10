FROM python:3.11-alpine
RUN apk add --no-cache git docker-cli
RUN git config --global --add safe.directory /home/alex/docker/landing-page
WORKDIR /app
COPY webhook-server.py .
CMD ["python", "webhook-server.py"]
