# communication_service.py

from flask import Flask, jsonify
import requests

app = Flask(__name__)

customer_service_url = "http://customer-service:5000/api/customer"

@app.route('/api/communication', methods=['GET'])
def get_communication_info():
    customer_info = requests.get(customer_service_url).json()
    return jsonify({"message": "Communication information from Communication Service", "customer_info": customer_info})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)