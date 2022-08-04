# uvicorn ffq_api.app:app --reload

import argparse
from datetime import datetime
from enum import Enum
import re
from typing import Optional

from fastapi import FastAPI, Request
from . import __version__
from ffq import __version__ as ffq_version
from ffq import main as ffq_main


# Define enum types for the API endpoint
class NamedEnum(str, Enum):
    pass

LinkType = NamedEnum("LinkType", {v: v for v in ["ftp", "aws", "gcp", "ncbi"]})
SearchType = NamedEnum("SearchType", {v: v for v in ffq_main.SEARCH_TYPES})


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
    search_type: Optional[SearchType] = None,
    level: Optional[int] = None,
    links: Optional[LinkType] = None,
):
    """
    Perform a query with ffq.

    :param accession_str: One or multiple SRA / GEO / ENCODE / ENA / EBI-EMBL / DDBJ / Biosample accessions, DOIs, or paper titles
    :param search_type:   UNUSED
    :param level:         Max depth to fetch data within accession tree
    :param links:         Retrieve only links from one of 'ftp', 'aws', 'gcp', or 'ncbi'
    """
    request_start = datetime.now()

    # Parse arguments
    args = argparse.Namespace()
    args.IDs = re.split(";| |,", accession_str)
    args.o = None
    args.t = search_type
    args.l = level
    args.ftp = (links == "ftp")
    args.aws = (links == "aws")
    args.gcp = (links == "gcp")
    args.ncbi = (links == "ncbi")
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
                "links": links,
            },
            "request": {
                "start": request_start.isoformat(),
                "finish": request_finish.isoformat(),
                "duration_seconds": (request_finish - request_start).total_seconds(),
            },
        }
    }
