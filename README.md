# biodataexplorer

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
