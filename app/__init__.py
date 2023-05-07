# src/app/__init__.py

from flask import Flask, render_template

# Main definitions
app = Flask(__name__)

# Other imports for the app
@app.route("/")
def index() -> dict:
    return render_template("index.html")
