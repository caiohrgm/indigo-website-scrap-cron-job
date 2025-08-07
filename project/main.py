from flask import Flask, jsonify
from scrap.scrap import run_scraping

app = Flask(__name__)

@app.route("/")
def home():
    return "API do scraper está no ar!"

@app.route("/run-scraping")
def run():
    data = run_scraping()
    return jsonify({"status": "ok", "results": data})

# Adicione isso no final:
if __name__ == "__main__":
    app.run(debug=True)
