#server
from flask import Flask, request, jsonify

app = Flask("Fahrenheit to Celsius")

@app.route('/convert', methods=['POST'])
def convert_temp():
    try:
        data = request.get_json()
        fahrenheit = data['fahrenheit']

        celsius = (fahrenheit - 32) * 5/9

        return jsonify({
            "Result": f"{fahrenheit}°F ==> {format(celsius, '.2f')}°C"
        })

    except Exception as e:
        return jsonify({"Error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=8796)