from flask import Flask,Response
import xml.etree.ElementTree as ET
app=Flask(__name__)
@app.route('/',methods=['GET'])
def Welcome():
    return "Welcome to Python Service"
if __name__=="__main__":
    app.run()

    