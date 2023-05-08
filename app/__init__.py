# app/__init__.py

"""
    Date: 05/2023
    :copyright: (c) 2023 Juan Carcedo, All rights reserved.
    :licence: MIT, see LICENSE.txt for further details.
    ::Details: Main app.
        Logics included:
        - Database management: db.py
        - Routes/views: views.py
        - Bookstore logics: bookstore.py
        - Handle erros: error_handler.py
"""

from flask import Flask

# Main definitions
app = Flask(__name__)

#### Other imports for the app and routes ####
### Database management =============================================
# from . import db
# Init database

### Routes ==========================================================
from . import views

### Auth ===========================================================
# from . import auth

### Bookstore logic ================================================
from . import bookstore

### Error handler: =================================================
from . import error_handler


### Checks app =====================================================
@app.route("/check-status", methods=["GET"])
def status_connection() -> tuple:
    """
    Check status of the application.
    :return: tuple
        dict: status OK // if error nothing delivered.
        http status code:
            200 Found -- Code: OK
    """
    response: tuple = {"status": "OK"}, 200
    return response
