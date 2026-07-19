from flask import Flask, render_template_string
import psycopg2
import os

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

HOME_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Flask + PostgreSQL * Docker * Project</title>
<style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        background: linear-gradient(135deg, #1e3c72, #2a5298);
        min-height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .card {
        background: #ffffff;
        padding: 40px 50px;
        border-radius: 16px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        text-align: center;
        max-width: 480px;
    }
    .badge {
        display: inline-block;
        background: #2a5298;
        color: white;
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 12px;
        letter-spacing: 1px;
        text-transform: uppercase;
        margin-bottom: 20px;
    }
    h1 {
        color: #1e3c72;
        font-size: 26px;
        margin-bottom: 10px;
    }
    p.subtitle {
        color: #555;
        margin-bottom: 20px;
        font-size: 15px;
    }
    .tag {
        font-weight: 600;
        color: #2a5298;
    }
    .status {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: #eafaf1;
        color: #1e7e34;
        padding: 8px 16px;
        border-radius: 8px;
        font-size: 14px;
        font-weight: 600;
    }
    .dot {
        width: 10px;
        height: 10px;
        background: #28a745;
        border-radius: 50%;
        animation: pulse 1.5s infinite;
    }
    @keyframes pulse {
        0% { opacity: 1; }
        50% { opacity: 0.4; }
        100% { opacity: 1; }
