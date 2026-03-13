from flask import Flask, request, jsonify

app = Flask("Prime Number Service")

def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


@app.route('/prime', methods=['POST'])
def check_prime():
    try:
        data = request.get_json()
        num = data['number']

        if is_prime(num):
            result = f"{num} is a Prime Number"
        else:
            result = f"{num} is NOT a Prime Number"

        return jsonify({"Result": result})

    except Exception as e:
        return jsonify({"Error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=8796)