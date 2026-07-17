from flask import Flask
import psycopg2
import os

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


@app.route("/")
def home():
    return "Hello from Flask + PostgreSQL Docker Project! JEENI HERE"


@app.route("/health")
def health():
    return "Application is running"


app.run(host="0.0.0.0", port=5000)
