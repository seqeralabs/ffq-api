# uvicorn ffq_api.app:app --reload

import argparse
from datetime import datetime
from enum import Enum
import re
from typing import Union

from fastapi import FastAPI, Request
from . import __version__
from ffq import __version__ as ffq_version
from ffq import main as ffq_main

# Build an Enum class for FastAPI that dynamically
# contains the ffq SEARCH_TYPES
class TempEnum(str, Enum):
    pass


Search_Types = TempEnum("Search_Types", {st: st for st in ffq_main.SEARCH_TYPES})

# Initialise the FastAPI app
app = FastAPI()


@app.get("/")
def read_root(request: Request):
    return {
        "message": "Welcome to the ffq API",
        "documentation_url": f"{request.url._url}docs",
        "meta": {
            "ffq_api_version": __version__,
            "ffq_version": ffq_version,
        },
    }


@app.get("/v1alpha1/{accession_str}")
def read_item(
    accession_str: str,
    search_type: Union[Search_Types, None] = None,
    ftp: bool = False,
    aws: bool = False,
    gcp: bool = False,
    ncbi: bool = False,
    level: Union[int, None] = None,
):
    request_start = datetime.now()
    accessions = re.split(";| |,", accession_str)

    args = argparse.Namespace()
    args.IDs = accessions  # One or multiple SRA / GEO / ENCODE / ENA / EBI-EMBL / DDBJ / Biosample accessions DOIs, or paper titles
    args.o = None  # Path to write metadata (default: standard out)
    args.t = search_type
    args.l = level  # Max depth to fetch data within accession tree
    args.ftp = ftp  # Return FTP links
    args.aws = aws  # Return AWS links
    args.gcp = gcp  # Return GCP links
    args.ncbi = ncbi  # Return NCBI links
    args.split = False  # Split output into separate files by accession
    args.verbose = False  # Print debugging information

    results = ffq_main.run_ffq(args)
    request_finish = datetime.now()
    results["meta"] = {
        "ffq_api_version": __version__,
        "ffq_version": ffq_version,
        "query": {
            "IDs": accession_str,
            "search_type": search_type,
            "level": level,
            "ftp": ftp,
            "aws": aws,
            "gcp": gcp,
            "ncbi": ncbi,
        },
        "request": {
            "start": request_start.isoformat(),
            "finish": request_finish.isoformat(),
            "duration_seconds": (request_finish - request_start).total_seconds(),
        },
    }

    return results
