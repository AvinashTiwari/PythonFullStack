from flask import Flask, jsonify, request

app = Flask(__name__)
stores = [{
    'name':'My wonderful store',
    'items' : [
       {
        'name':'My Item',
        'price': 15.01
       }
    ]
}]

@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
    'name': request_data['name'],
    'item':[]
    }
    stores.append(new_store)
    return jsonify(new_store)


@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message':'store not found'})

@app.route('/store')
def get_store_data():
    return jsonify({'stores': stores})

@app.route('/store/<string:name>', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
            'name':request_data['name'],
            'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(store)
    return jsonify({'message':'store not found'})




@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'item':store['items']})
    return jsonify({'message':'store not found'})

app.run(port=5000)
