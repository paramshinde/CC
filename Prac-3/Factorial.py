#server
from flask import Flask, request, jsonify

app = Flask("Factorial Service")

def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact

@app.route('/factorial', methods=['POST'])
def calculate_factorial():
    try:
        data = request.get_json()
        number = data['number']
        
        result = factorial(number)

        return jsonify({
            "Number": number,
            "Factorial": result
        })

    except Exception as e:
        return jsonify({"Error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=8796)