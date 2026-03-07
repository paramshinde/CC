from flask import Flask,request,send_from_directory
import os

app=Flask(__name__)
upload='uploads'
os.makedirs(upload,exist_ok=True)

@app.route('/upload',methods=['POST'])
def upload_file():
    file=request.files.get('file')
    if file:
        filepath=os.path.join(upload,file.filename)
        file.save(filepath)
        return {"message" : "success"},200
    return {"error": "file not provided"}, 400

@app.route('/down/<file>',methods=['GET'])
def downfile(file):
    try:
        return send_from_directory(upload,file,as_attachment=True)
    except FileNotFoundError:
        return {"error": "file not provided"}, 400

if __name__=="__main__":
    app.run(debug=True)