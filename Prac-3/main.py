from flask import Flask,jsonify,request
app=Flask("RS to $")
@app.route('/convert',methods=['POST'])
def convert():
    try:
        data=request.get_json()
        amtrs=data['rs']
        rate=0.012
        dollar=amtrs*rate
        return jsonify({'Result':f"Rs{amtrs}==>${format(dollar,'.4f')}"})
    except Exception as E:
        return jsonify({"Error":str(E)})
if __name__=="__main__":
    app.run(debug=True,port=9876)