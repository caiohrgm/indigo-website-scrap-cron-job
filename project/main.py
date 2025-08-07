from flask import Flask, jsonify
from flask_cors import CORS
import json
from scrap.scrap import run_scraping

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["https://www.indigotechnologies.wiki.br", "http://localhost:5173/"]}})

@app.route("/")
def home():
    return "Scraper API is running!"

@app.route("/run-scraping")
def run():
    data = run_scraping()
    return jsonify({"status": "ok", "results": data})

@app.route("/update-system-data")
def get_dados():
    with open("data/systems.json", encoding="utf-8") as f:
        data = json.load(f)
    return jsonify(data)

# Adicione isso no final:
if __name__ == "__main__":
    app.run(debug=True)
