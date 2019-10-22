import grpc
from concurrent import futures
import time
import threading


import calculator_pb2
import calculator_pb2_grpc


class Listener(calculator_pb2_grpc.CalculatorServicer):

        def sum(self, request, context):
                response = calculator_pb2.RNumber()
                response.value = request.value + request.value2
                return response

        def mult(self, request, context):
                response = calculator_pb2.RNumber()
                response.value = request.value * request.value2
                return response


        def div(self, request, context):
                response = calculator_pb2.RNumber()
                response.value = request.value / request.value2
                return response


        def sub(self, request, context):
                response = calculator_pb2.RNumber()
                response.value = request.value - request.value2
                return response

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))


calculator_pb2_grpc.add_CalculatorServicer_to_server(Listener(), server)

print('Starting server. Listening on port 5001')
server.add_insecure_port('[::]:5001')
server.start()


try:
  while True:
      time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
