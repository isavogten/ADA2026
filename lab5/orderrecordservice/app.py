from flask import Flask, request
from flask import make_response
from resources.order import Order, Orders
from flask_cors import CORS
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # This is not recommend for production.
orders = Orders()
placeRecord = Order()


@app.route('/orders/<string:id>', methods=['GET'])
def get_order(id):
    res = make_response(placeRecord.get(id))
    res.headers.add('Cache-control', "max-age=180, public")
    return res


@app.route('/orders/<string:id>', methods=['PUT'])
def update_order(id):
    return placeRecord.put(id, int(request.args.get('rating')))


@app.route('/orders/<string:id>', methods=['DELETE'])
def delete_orders(id):
    return placeRecord.delete(id)


@app.route('/orders/', methods=['POST'])
def create_order():
    return orders.post(request)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
