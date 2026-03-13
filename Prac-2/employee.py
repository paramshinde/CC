from flask import Flask, request, jsonify, Response
import xml.etree.ElementTree as ET

app = Flask("Employee App")

employees = [
    {"id":1,"employee_name":"Rahul","phone_no":"9876543210","department":"IT"},
    {"id":2,"employee_name":"Priya","phone_no":"9123456780","department":"HR"}
]

# Get all employees in JSON
@app.route('/employees',methods=['GET'])
def get_employees():
    if len(employees)!=0:
        return jsonify({"Employees":employees})
    else:
        return jsonify({"Error":"Employees Not Found"}),400


# Get all employees in XML
@app.route('/all_employees',methods=['GET'])
def all_employees():

    root=ET.Element('employees')

    for emp in employees:
        xmlemp=ET.SubElement(root,'employee')
        xmlemp.set('id',str(emp['id']))

        ename=ET.SubElement(xmlemp,'employee_name')
        ename.text=emp['employee_name']

        ephone=ET.SubElement(xmlemp,'phone_no')
        ephone.text=emp['phone_no']

        edept=ET.SubElement(xmlemp,'department')
        edept.text=emp['department']

    xml_string=ET.tostring(root)

    return Response(xml_string,mimetype='text/xml')


# Get specific employee by id
@app.route('/employee/<int:eid>',methods=['GET'])
def get_employee(eid):

    emp=next((e for e in employees if e['id']==eid),None)

    if emp:
        return jsonify(emp)
    else:
        return jsonify({"Error":"Employee Not Found"}),404


# Add new employee
@app.route('/employee/add',methods=['POST'])
def add_employee():

    data=request.get_json()

    new_emp={
        "id":len(employees)+1,
        "employee_name":data['employee_name'],
        "phone_no":data['phone_no'],
        "department":data['department']
    }

    employees.append(new_emp)

    return jsonify({"New Employee Added":new_emp,"All Employees":employees})


# Update employee
@app.route('/employee/edit/<int:eid>',methods=['PUT'])
def update_employee(eid):

    emp=next((e for e in employees if e['id']==eid),None)

    if emp:
        data=request.get_json()
        emp.update(data)
        return jsonify(emp)
    else:
        return jsonify({"Error":"Employee Not Found"}),400


# Delete employee
@app.route('/employee/remove/<int:eid>',methods=['DELETE'])
def remove_employee(eid):

    emp=next((e for e in employees if e['id']==eid),None)

    if emp:
        employees.remove(emp)
        return jsonify({"MSG":"Employee Deleted"})
    else:
        return jsonify({"Error":"Employee Not Found"}),400


if __name__=="__main__":
    app.run(debug=True,port=2546)