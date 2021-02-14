""" Testing part.
    from root run $ python -m pytest
    this adds root to python path and allow for import api

    for dev run local server $ uvicorn main:app --reload
"""
# import pytest
from fastapi.testclient import TestClient
#
import api.main

client = TestClient(api.main.app)


def test_read_root_url():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "from main FastAPI & API Gateway"}


def f():
    return 3


def test_function():
    assert f() == 3
