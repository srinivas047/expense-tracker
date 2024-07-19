import boto3
from flask import Flask, request, jsonify

app = Flask(__name__)
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Expenses')

@app.route('/add', methods=['POST'])
def add_expense():
    data = request.json
    table.put_item(Item={'id': data['id'], 'amount': data['amount'], 'category': data['category'], 'description': data['description']})
    return jsonify({'message': 'Expense added'})

@app.route('/view', methods=['GET'])
def view_expenses():
    response = table.scan()
    return jsonify({'expenses': response['Items']})
