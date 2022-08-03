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


# Define an Enum class for FastAPI that contains the ffq SEARCH_TYPES
class NamedEnum(str, Enum):
    pass

SearchTypes = NamedEnum("SearchTypes", {st: st for st in ffq_main.SEARCH_TYPES})


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
    search_type: Union[SearchTypes, None] = None,
    ftp: bool = False,
    aws: bool = False,
    gcp: bool = False,
    ncbi: bool = False,
    level: Union[int, None] = None,
):
    """
    Perform a query with ffq.

    :param accession_str: One or multiple SRA / GEO / ENCODE / ENA / EBI-EMBL / DDBJ / Biosample accessions, DOIs, or paper titles
    :param search_type:
    :param ftp:           Return FTP links
    :param aws:           Return AWS links
    :param gcp:           Return GCP links
    :param ncbi:          Return NCBI links
    :param level:         Max depth to fetch data within accession tree
    """
    request_start = datetime.now()

    # Parse arguments
    args = argparse.Namespace()
    args.IDs = re.split(";| |,", accession_str)
    args.o = None
    args.t = search_type
    args.l = level
    args.ftp = ftp
    args.aws = aws
    args.gcp = gcp
    args.ncbi = ncbi
    args.split = False
    args.verbose = False

    # Perform query
    results = ffq_main.run_ffq(args)

    request_finish = datetime.now()

    # Return API response
    return {
        "results": results,
        "meta": {
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
    }
