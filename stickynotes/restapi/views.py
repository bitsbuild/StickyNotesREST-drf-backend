from django.shortcuts import render
from rest_framework.views import APIView
from restapi.serializers import NoteSerializer
from rest_framework.response import Response
from rest_framework import status
from restapi.models import Note
class NoteCR(APIView):
    def post(self,request):
        ser = NoteSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"status":str(ser.data)},status=status.HTTP_201_CREATED)
        else:
            return Response({"status":str(ser.errors)},status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        try:
            note_list = Note.objects.all()
            serialized_note_list = NoteSerializer(note_list,many=True)
            return Response(serialized_note_list.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(serialized_note_list.errors,status=status.HTTP_400_BAD_REQUEST)
        
class NoteUD(APIView):
        def put(self,request,id):
            toupdate_note = Note.objects.get(pk=id)
            ser = NoteSerializer(toupdate_note,data=request.data)
            if ser.is_valid():
                ser.save()
                return Response(ser.data,status=status.HTTP_200_OK)
            else:
                return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
        def delete(self,request,id):
            try:
                Note.objects.get(pk=id).delete()
                return Response({"status":"selected item deleted"},status=status.HTTP_200_OK)
            except Exception as e:
                return Response({"status":"deletion process failed"},status=status.HTTP_400_BAD_REQUEST)