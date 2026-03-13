from zeep import Client

client = Client('http://127.0.0.1:10000/?wsdl')

num = int(input("Enter number: "))

result = client.service.square_number(num)

print(f"Square of {num} is: {result}")