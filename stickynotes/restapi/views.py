from django.shortcuts import render
from rest_framework.views import APIView
from restapi.serializers import NoteSerializer
from rest_framework.response import Response
from rest_framework import status
class NoteCUD(APIView):
    def post(self,request):
        ser = NoteSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"status":str(ser.data)},status=status.HTTP_201_CREATED)
        else:
            return Response({"status":str(ser.errors)},status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,id):
        pass
    def delete(self,request,id):
        pass