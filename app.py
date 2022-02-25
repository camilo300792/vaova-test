from flask import Flask, jsonify, request, Response
from hotel_collection import HotelCollection
import helpers

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'message': "Welcome to vaova test!"})


@app.route('/hotels', methods=['GET', 'POST'])
def hotels():
    collection = HotelCollection()
    
    if request.method == 'POST':
        try:
            insert_id = collection.write(request.json)
            return jsonify({"hotel_id": insert_id}), 201
        except Exception as e:
            return jsonify({"message": str(e)}), 404

    name = request.args.get('name')
    hotels = collection.read(name=name)
    return jsonify(hotels), 200

@app.route('/hotels/<hotel_id>', methods=['DELETE'])
def delete(hotel_id):
    collection = HotelCollection()
    collection.delete(hotel_id)
    return Response(status=204)



