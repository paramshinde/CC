from zeep import Client
client=Client('http://127.0.0.1:10000/?wsdl')
res_add=client.service.add_num(5,10)
res_sub=client.service.sub_num(5,10)
print(f"Addititon :{res_add}")
print(f"Subtraction :{res_sub}")