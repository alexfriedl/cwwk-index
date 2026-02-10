FROM python:3.11-alpine
RUN apk add --no-cache git docker-cli
WORKDIR /app
COPY webhook-server.py .
CMD ["python", "webhook-server.py"]
