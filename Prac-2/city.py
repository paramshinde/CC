from flask import Flask, request, jsonify

app = Flask("City API")

cities = [
    {"city_name": "Mumbai", "district_name": "Mumbai City", "population": 12442373},
    {"city_name": "Pune", "district_name": "Pune", "population": 3124458}
]

# GET all cities
@app.route('/cities', methods=['GET'])
def get_cities():
    if len(cities) != 0:
        return jsonify({"Cities": cities})
    else:
        return jsonify({"Error": "No Cities Found"}), 404


# GET specific city
@app.route('/city/<string:cname>', methods=['GET'])
def get_city(cname):
    city = next((c for c in cities if c['city_name'].lower() == cname.lower()), None)
    if city:
        return jsonify(city)
    else:
        return jsonify({"Error": "City not found"}), 404


# ADD new city
@app.route('/city/add', methods=['POST'])
def add_city():
    data = request.get_json()

    new_city = {
        "city_name": data['city_name'],
        "district_name": data['district_name'],
        "population": data['population']
    }

    cities.append(new_city)

    return jsonify({"Message": "City Added", "City": new_city})


# UPDATE city
@app.route('/city/update/<string:cname>', methods=['PUT'])
def update_city(cname):
    city = next((c for c in cities if c['city_name'].lower() == cname.lower()), None)

    if city:
        data = request.get_json()
        city.update(data)
        return jsonify({"Updated City": city})
    else:
        return jsonify({"Error": "City not found"}), 404


# DELETE city
@app.route('/city/delete/<string:cname>', methods=['DELETE'])
def delete_city(cname):
    city = next((c for c in cities if c['city_name'].lower() == cname.lower()), None)

    if city:
        cities.remove(city)
        return jsonify({"Message": "City Deleted"})
    else:
        return jsonify({"Error": "City not found"}), 404


if __name__ == "__main__":
    app.run(debug=True, port=5000)