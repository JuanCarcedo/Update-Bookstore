# tests/test_app.py

"""
    Date: 05/2023
    :copyright: (c) 2023 Juan Carcedo, All rights reserved.
    :licence: MIT, see LICENSE.txt for further details.
    :: Details: Test basic configuration and app.
"""

def test_status_ok(client):
    """Check if app is running OK"""
    response = client.get("/check-status")
    assert response.status_code == 200
    assert response.json["status"] == "OK"
