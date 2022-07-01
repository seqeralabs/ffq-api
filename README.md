# ffq-api

A minimal wrapper to make [ffq](https://github.com/pachterlab/ffq) searches available via a REST API.

> `ffq` receives an accession and returns the metadata for that accession as well as the metadata for all downstream accessions following the connections between GEO, SRA, EMBL-EBI, DDBJ, and Biosample.
>
> If you use ffq in a publication, please the [cite*](#cite):
>
> ```
> Gálvez-Merchán, Á., et al. (2022). Metadata retrieval from sequence databases with ffq. bioRxiv 2022.05.18.492548.
> ```
> The manuscript is available here: <https://doi.org/10.1101/2022.05.18.492548>.

For more information about `ffq`, please visit the GitHub repository: <https://github.com/pachterlab/ffq>

## Get started

The query service aims to mimic the functionality of the `ffq` command line tool. It returns the same JSON, with the exception of an additional `meta` field.

The public instance of **ffq-api** is accessible at: <https://ffq.seqera.io>

Extensive API documentation and an interactive testing interface is available at <https://ffq.seqera.io/docs>

## Example usage

Usage is via the `/v1alpha1/` endpoint and takes one or more accessions (comma separated) as the final part of the path.

The response is pure JSON, meaning it plays well with tools such as [`jq`](https://stedolan.github.io/jq/). For example:

```bash
curl https://ffq.seqera.io/v1alpha1/SRR9990627 | jq
```

There are some additional `GET` parameters available to customise results, which mimic the command-line interface flags. For more information about these, please see the [API documentation](https://ffq.seqera.io/docs) and the [`ffq` documentation](https://github.com/pachterlab/ffq#usage).

> ⚠️ Note that `ffq` interacts with a lot of databases via secondary API calls. This wrapper is synchronous, meaning that responses may take a long time.

## Installation

If you wish, you may run your own instance of ffq-api.

First, clone the repo and install the package and its dependencies:

```bash
pip install .
```

The server runs with FastAPI. There are [different ways](https://fastapi.tiangolo.com/deployment/) to deploy, but the simplest when running locally is to use [uvicorn](https://www.uvicorn.org) with the bundled script:

```bash
./launch.sh
```

The log should tell you the URL, but it's typically [`http://127.0.0.1:8000`](http://127.0.0.1:8000)

You can find the interactive API documentation at the URL [`/docs`](http://127.0.0.1:8000/docs).

## Cite

If you use this tool, please cite [`ffq`](https://github.com/pachterlab/ffq) which powers the results:

```bibtex
@article{galvez2022metadata,
  title={Metadata retrieval from sequence databases with ffq},
  author={G{\'a}lvez-Merch{\'a}n, {\'A}ngel and Min, Kyung Hoi Joseph and Pachter, Lior and Booeshaghi, A. Sina},
  year={2022}
}
```
