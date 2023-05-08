# app/error_handler.py

"""
    Date: 05/2023
    :copyright: (c) 2023 Juan Carcedo, All rights reserved.
    :licence: MIT, see LICENSE.txt for further details.
    :: Details: Handle exceptions (like 404).
"""
from app import app
from flask import render_template


@app.errorhandler(404)
def page_not_found(e) -> tuple:
    """404 Error"""
    return render_template("404.html"), 404
