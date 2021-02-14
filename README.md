# fastAPI-lambda
 * 2021-02-13 cloned from cryptoAPI to play with fastAPI and AWS lambda
   * https://towardsdatascience.com/fastapi-aws-robust-api-part-1-f67ae47390f9

 * python modules
   * mangum asgi adaptor for lambda https://pypi.org/project/mangum/
   * uvicorn python ASGI server for local run.

# Setup
 1. $ python3 -m venv venv
 1. $ source venv/bin/activate
 1. $ pip install -r api/requirements.txt
 1. $ cd api; $ uvicorn api/main:app --reload
# cryptoAPI
A demo API demonstrating how to create a Python-based REST API with FastAPI, Mangum, Amazon Lambda and API Gateway
