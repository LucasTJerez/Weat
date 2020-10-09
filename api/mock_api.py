import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True
data = {}

@app.route('/', methods=['GET'])
def home():
    data = init()
    if data is None:
        return "<h1>Error</h1><p>Data could not be found. Please try again.</p>"
    return "<h1>API</h1><p>This is a mock API for managing Weat orders. Yum!</p>"

@app.route('/menu-items', methods=['GET'])
def menu_items():
    restaurant = None
    if 'restaurant' in request.args:
        restaurant = request.args['restaurant']
    if restaurant in data:
        return jsonify(data[restaurant])
    else:
        return "<h1>Error</h1><p>Restaurant " + restaurant + " could not be found.</p>" 

@app.route('/num-orders', methods=['GET'])
def num_orders():
    restaurant = None
    item = None
    if 'restaurant' in request.args:
        restaurant = request.args['restaurant']
    if 'item' in request.args:
        item = request.args['item']
    if restaurant in data:
        orders = data[restaurant][1]
        if item in orders:
            return jsonify(orders[item])
        else:
            return "<h1>Error</h1><p>Item " + item + " could not be found in restaurant " + restaurant + ".</p>" 
    else:
        return "<h1>Error</h1><p>Restaurant " + restaurant + " could not be found.</p>" 

@app.route('/get-restaurants', methods=['GET'])
def get_restaurants():
    return jsonify([restaurant for restaurant in data])

def init():
    file = None
    try:
        file = open('data/mock_database.csv')
    except:
        return None
    for line in file:
        readData(line.rstrip('\n').split(','))
    return data

def readData(line):
    restaurant = line[0]
    address = line[1]
    item = line[2]
    quantity = line[3]
    if restaurant in data:
        data[restaurant][1][item] = quantity
    else:
        data[restaurant] = (address, {item: quantity})

app.run()
