# ffq-api

Expose [ffq](https://github.com/pachterlab/ffq) searches via an API wrapper.

## Get started 

The query service is accessible via the endpoint  https://ffq.seqera.io/ffq and mimics the functionality of the `ffq` tool. 

For example:

```
curl https://ffq.seqera.io/ffq/SRR9990627?aws=true | jq
```

See API docs at [this link](https://ffq.seqera.io/docs).

## Installation

For now, clone the repo and install locally:

```bash
pip install -e .
```

## Running the server

The server runs with FastAPI. There are [different ways](https://fastapi.tiangolo.com/deployment/) to deploy, but the simplest when running locally is to use [uvicorn](https://www.uvicorn.org) with the bundled script:

```bash
./launch.sh
```

The log should tell you the URL, but it's typically [`http://127.0.0.1:8000`](http://127.0.0.1:8000)

You can find the interactive API documentation at the URL [`/docs`](http://127.0.0.1:8000/docs).
