from setuptools import setup

setup(
    name="ffq-api",
    install_requires=[
        "fastapi>=0.68.0",
        "pydantic>=1.8.0",
        "uvicorn>=0.15.0",
        "ffq>=0.2.1",
    ],
)
