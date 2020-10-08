import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True
data = {}

@app.route('/', methods=['GET'])
def home():
    data = init()
    print(data)
    if data is None:
        return "<h1>Error</h1><p>Data could not be found. Please try again.</p>"
    return "<h1>API</h1><p>This is a mock API for managing Weat orders. Yum!</p>"

@app.route('/menu-items', methods=['GET'])
def menu_items():
    if 'restaurant' in request.args:
        restaurant = request.args['restaurant']
    if restaurant in data:
        return jsonify(data[restaurant])
    else:
        return "<h1>Error</h1><p>Restaurant " + restaurant + " could not be found</p>" 

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
    orders = (line[2], line[3])
    if restaurant in data:
        data[restaurant][1].append(orders)
    else:
        data[restaurant] = (address, [orders])

app.run()