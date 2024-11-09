from flask import jsonify, request
from src import app  
from .query import answer_query

@app.route('/')
def index():
    return 'Welcome to the this Q&A service!'

@app.route('/answer', methods=['POST'])
def get_answer():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400
        
    query = request.json.get('query')
    if not query:
        return jsonify({"error": "Query parameter is required"}), 400
        
    response = answer_query(query)
    if response is None:
        return jsonify({"error": "Failed to generate response"}), 500
        
    return jsonify({
        "response": str(response)
    })