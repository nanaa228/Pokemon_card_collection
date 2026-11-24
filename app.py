from flask import Flask, jsonify, request
import os
import secrets
from dotenv import load_dotenv
from flask_cors import CORS
from database import get_all_cards, add_card, find_cards_by_set, delete_card, get_rarity_report
load_dotenv()
ADMIN_TOKEN=os.getenv("ADMIN_TOKEN")
app = Flask(__name__)
CORS(app,
     origins=["https://nanascollection.pp.ua"])
@app.route("/")
def home():
    return "Welcome to Pokemon Card Collection!"
@app.route("/cards", methods=["GET"])
def show_cards():
    card_set = request.args.get("card_set")
    if card_set:
        cards = find_cards_by_set(card_set.strip())
    else:
        cards = get_all_cards()
    return jsonify(cards)
@app.route("/cards", methods=["POST"])
def create_card():
    token = request.headers.get("X-Admin-Token", "")
    if not ADMIN_TOKEN or not secrets.compare_digest(token, ADMIN_TOKEN):
        return jsonify({"Error": "Access denied"}), 403
    data = request.get_json()
    if not isinstance(data, dict):
        return jsonify({"error": "Invalid data format"}), 400
    required = ["name", "card_set", "rarity", "number", "artist"]
    for field in required:
        if not isinstance(data.get(field), str) or not data.get(field).strip():
            return jsonify({"error": f"Field '{field}' is required and must be a non-empty string"}), 400
    card_id = add_card(data["name"].strip(), data["card_set"].strip(), data["rarity"].strip(), data["number"].strip(), data["artist"].strip())
    return jsonify({"message": "Card added successfully", "Id": card_id}), 201 
@app.route("/cards/<int:card_id>", methods=["DELETE_DISABLED"])
def remove_card(card_id):
    return jsonify ({"Error": "Access denied"}), 403
    deleted = delete_card(card_id)
    if deleted:
        return jsonify({"message": "Card deleted successfully"}), 200
    return jsonify({"error": "Card not found"}), 404
@app.route("/report", methods=["GET"])
def show_report():
    report = get_rarity_report()
    return jsonify(report)
if __name__ == "__main__":
    app.run(debug=True)
