import grpc
import calculator_pb2
import calculator_pb2_grpc

channel = grpc.insecure_channel('localhost:5001')

stub = calculator_pb2_grpc.CalculatorStub(channel)

while True:

    print("Selecione a operação (ex: '+', '-', '*' ou '/'): ")
    oper = input()

    print("Enter first number")
    x = input()

    print("Enter second number")
    y = input()

    number = calculator_pb2.Numbers(value=float(x),value2=float(y))

    if oper == "+":
        response = stub.sum(number)
    elif oper == "-":
        response = stub.sub(number)
    
    elif oper == "*":
        response = stub.mult(number)

    elif oper == "/":
        response = stub.div(number)

    print("Resultado: ")
    print(response.value)
