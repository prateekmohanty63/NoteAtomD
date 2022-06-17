from django.shortcuts import render
from rest_framework.response import Response
from .models import Note
from .serializers import NoteSerializer


def getNoteDetails(request,pk):
    notes=Note.objects.get(id=pk)
    serializer=NoteSerializer(notes,many=False)
    return Response(serializer.data)

# @api_view(['PUT'])
def updateNote(request,pk):
    data=request.data
    print(data)
    note=Note.objects.get(id=pk)
    serializer=NoteSerializer(instance=note,data=data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


    