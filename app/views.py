# app/views.py

"""
    Date: 05/2023
    :copyright: (c) 2023 Juan Carcedo, All rights reserved.
    :licence: MIT, see LICENSE.txt for further details.
    :: Details: Flow of main views.
"""
from app import app
from flask import render_template


@app.route("/", methods=["GET"])
@app.route("/index", methods=["GET"])
def index() -> dict:
    """Landing Page -- Home"""
    return render_template("index.html")
