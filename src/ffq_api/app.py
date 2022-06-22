# uvicorn ffq_api.app:app --reload

import re
from typing import Union

from fastapi import FastAPI, Request
from ffq import main as ffq_main

app = FastAPI()

@app.get("/")
def read_root(request: Request):
    return {
        "message": "Welcome to the ffq API",
        "documentation_url": f"{request.url._url}docs",
    }


@app.get("/v1alpha1/{accession_str}")
def read_item(accession_str: str, aws: bool = False):
    accession_strs = re.split(';| |,', accession_str)
    accessions = ffq_main.validate_accessions(accession_strs, ffq_main.SEARCH_TYPES)
    results = []
    for v in accessions:
        results.append(ffq_main.FFQ[v["prefix"]](v["accession"], 0))
    results

    keyed = {result["accession"]: result for result in results}
    links = []
    if aws:
        # get run files
        found_links = []
        ffq_main.findkey(keyed, "aws", found_links)
        links += found_links
    return links if len(links) else keyed
