# uvicorn ffq_api.app:app --reload

import argparse
from enum import Enum
import re
from typing import Union

from fastapi import FastAPI, Request
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

    return ffq_main.run_ffq(args)
