# tests/conftest.py

"""
    Date: 05/2023
    :copyright: (c) 2023 Juan Carcedo, All rights reserved.
    :licence: MIT, see LICENSE.txt for further details.
    :: Details: Setup test.
"""

import pytest
from app import app

@pytest.fixture()
def client():
    app.config["testing"] = True
    client = app.test_client()
    yield client
