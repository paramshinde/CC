from flask import Flask,request,jsonify,Response
import xml.etree.ElementTree as ET

app=Flask('Book App')
books=[{'id':1,'title':'CC & WSN','author':'XYZ'},
       {'id':2,'title':'EH & DS','author':'ABC'}]

#get all books in json
@app.route('/books',methods=['GET'])
def get_books():
    if len(books)!=0:
        return jsonify({"Result":books})
    else:
        return jsonify({'Error':"Books Not Found"}),400

#get all books
@app.route('/all_books',methods=['GET'])
def all_books():
    root=ET.Element('book')
    for book in books:
        xmlbook=ET.SubElement(root,'book')
        xmlbook.set('id',str(book['id']))
        btitle=ET.SubElement(xmlbook,'title')
        btitle.text=book['title']
        bauthor=ET.SubElement(xmlbook,'author')
        bauthor.text=book['author']
    xml_string=ET.tostring(root)
    return Response(xml_string,mimetype='text/xml')

#get a specific book id
@app.route("/book/<int:b_id>",methods=['GET'])
def get_a_Book(b_id):
    book=next((b for b in books if b['id']==b_id),None)
    if book:
        return jsonify(book)
    else:
        return jsonify({"Error"}),404
    
#update a book by id
@app.route("/book/edit/<int:b_id>",methods=['PUT'])
def update_book(b_id):
    book=next((b for b in books if b['id']==b_id),None)
    if book:
        data=request.get_json()
        book.update(data)
        return jsonify(book)
    else:
        return jsonify({"Error"}),400

#add a new book
@app.route('/book/add',methods=['POST'])
def add_book():
    data=request.get_json()
    new_book={'id':len(books)+1,'title':data['title'],'author':data['author']}
    books.append(new_book)
    return jsonify({"New Book Added":new_book,"All Books":books})

#remove a book
@app.route('/book/remove/<int:bid>',methods=['DELETE'])
def remove_book(bid):
    book=next((b for b in books if b['id']==bid),None)
    if book:
        books.remove(book)
        return jsonify({'MSG':'Success'})
    else:
        return jsonify({"Error"}),400



if __name__=="__main__":
    app.run(debug=True,port=2546)