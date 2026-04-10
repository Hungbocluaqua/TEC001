from flask import Flask, jsonify
import json
app = Flask(__name__)
file = open("airports.json", "r")
airports = json.load(file)
file.close()
@app.route("/airport/<icao>")
def get_airport(icao):
    for airport in airports:
        if airport["icao"] == icao:
            return jsonify({
                "icao": airport["icao"],
                "name": airport["name"],
                "city": airport["city"],
                "country": airport["country"]
            })
    return jsonify({
        "error": "Airport not found"
    }), 404
app.run()