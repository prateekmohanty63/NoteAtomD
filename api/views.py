from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Note
from .serializers import NoteSerializer
# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
    return Response(routes)

# get all  notes
@api_view(['GET'])
def getNotes(request):
    notes=Note.objects.all().order_by('-updated')
    serializer=NoteSerializer(notes,many=True)
    return Response(serializer.data)

# get note by id
@api_view(['GET'])
def getNote(request,pk):
    notes=Note.objects.get(id=pk)
    serializer=NoteSerializer(notes,many=False)
    return Response(serializer.data)

# delete note
@api_view(['DELETE'])
def deleteNote(request,pk):
    note=Note.objects.get(id=pk)
    note.delete()

    return Response('Note was deleted')



# update note

@api_view(['PUT'])
def updateNote(request,pk):
    data=request.data
    print(data)
    note=Note.objects.get(id=pk)
    serializer=NoteSerializer(instance=note,data=data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

    