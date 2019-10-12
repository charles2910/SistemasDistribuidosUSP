import grpc
import calculator_pb2
import calculator_pb2_grpc

channel = grpc.insecure_channel('localhost:5001')

stub = calculator_pb2_grpc.CalculatorStub(channel)

print("Enter first number")
x = input()

print("Enter second number")
y = input()

number = calculator_pb2.Numbers(value=float(x),value2=float(y))

response = stub.sum(number)

print(response.value)
