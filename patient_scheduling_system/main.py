"""
main.py
Contains the main entry point of the application.
"""

from flask import Flask
from routes import patient_routes

app = Flask(__name__)

app.register_blueprint(patient_routes)

if __name__ == "__main__":
    app.run()
