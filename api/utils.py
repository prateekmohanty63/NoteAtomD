from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Note
from .serializers import NoteSerializer


# @api_view(['PUT'])
def updateNote(request,pk):
    data=request.data
    print(data)
    note=Note.objects.get(id=pk)
    serializer=NoteSerializer(instance=note,data=data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

    