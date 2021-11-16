from django.shortcuts import render
from django.core import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

import os
import os.path as osp
import sys
BUILD_DIR = osp.join(osp.dirname(osp.abspath(__file__)), "../build/service/")
sys.path.insert(0, BUILD_DIR)

import json
import grpc
import fib_pb2
import fib_pb2_grpc

from .models import History

# Create your views here.
class FibView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        decoded = request.body.decode('utf-8')
        body = json.loads(decoded)
        data = body['order']
        host='127.0.0.1:8080'
        with grpc.insecure_channel(host) as channel:
            stub = fib_pb2_grpc.FibCalculatorStub(channel)

            request = fib_pb2.FibRequest()
            try:
                order = int(data)
                request.order = order 
                response = stub.Compute(request)
                
                history = History(success=True, order = order, result = response.value)
                history.save()

                
                return Response(data={ 'success': True, 'data': response.value }, status=200)
            except ValueError:
                history = History(success=False, order = 0, result = 0)
                history.save()

                return Response(data={ 'success': False, 'data': "Not a number" }, status=400)

class LogView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        logs = History.objects.all()
        data = serializers.serialize('json', logs)
        return Response({"status": "success", "history": data}, status=200)           
