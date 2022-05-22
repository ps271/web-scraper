from flask import Blueprint, jsonify
from app.controller.flipkart import FlipkartController


flipkart_bp = Blueprint('api/flipkart', __name__, url_prefix='/webscraper/flipkart')
flipkart_c = FlipkartController()

@flipkart_bp.route('/laptops', methods=['GET'])
def laptops():
    json_response = flipkart_c.laptop_search()
    return json_response, 200



@flipkart_bp.route('/mobiles', methods=['GET'])
def mobiles():
    json_response = flipkart_c.mobile_search()