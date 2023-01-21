from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PersonSerializer
from .models import Person
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


@api_view(['GET', 'POST', 'PUT']) 
def home_API(request):
    data = {"animal":"perro"}
    if request.method == "POST":
        print("it was hit by post method")
        data = request.data
        serializer = PersonSerializer(data = data)
        if serializer.is_valid():
            print("entering")
            serializer.save()


    if request.method == "GET":
        print("it was hit by GET method")

    return Response(data, status=200)

@api_view(['GET', 'POST'])
def person(request):
    if request.method == "GET":
        queryset = Person.objects.all()
        serializer = PersonSerializer(queryset, many=True)
        return Response(serializer.data)
    
    else:
        data = request.data
        serializer = PersonSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)