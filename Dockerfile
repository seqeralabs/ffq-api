
# Docs: https://fastapi.tiangolo.com/deployment/docker/

# docker build -t ffq-api .
# docker run -d --name ffq-api-container -p 8000:8000 ffq-api
# Should be running at http://127.0.0.1 or similar

FROM python:3.9

WORKDIR /code

COPY ./ /code

RUN pip install --no-cache-dir --upgrade .

EXPOSE 8000

# If running behind a proxy like Nginx or Traefik add --proxy-headers
 CMD ["uvicorn", "ffq_api.app:app", "--host", "0.0.0.0", "--port", "8000"]
