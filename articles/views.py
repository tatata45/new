from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Acticle
from .serializers import ActicleSerializer


@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_acticle(request, pk):
    try:
        acticle = Acticle.objects.get(pk=pk)
    except Acticle.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ActicleSerializer(acticle)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = ActicleSerializer(acticle, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        acticle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def get_post(request):

    if request.method == 'GET':
        puppies = Acticle.objects.all()
        serializer = ActicleSerializer(puppies, many=True)
        return Response(serializer.data)


    if request.method == 'POST':
        data = {
            'name': request.data.get('name'),
            'description': request.data.get('description'),
            'category_id': int(request.data.get('category_id')),
        }
        serializer = ActicleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
