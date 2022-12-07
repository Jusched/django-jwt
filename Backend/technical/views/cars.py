# Rest Framework
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import serializers, status


# Django
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

# Local modules
from ..serializers import CarSerializer
from ..models import Car


@api_view(["GET"])
@permission_classes([AllowAny])
def ApiView(request):
    api_urls= {
        'all_cars': 'all/',
        'Add': 'create/',
        'Update': 'update/pk/',
        'Delete': 'delete/pk/',
    }
    return Response(api_urls)


@login_required
@api_view(['POST'])
def add_cars(request):

    car = CarSerializer(data=request.data)

# Validating
    if Car.objects.filter(**request.data).exists():
        raise serializers.ValidationError("This car already exists.")

    if car.is_valid():
        car.save()
        return Response(car.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
@permission_classes([AllowAny])
def view_cars(request):
    
    cars = Car.objects.all()
    serializer = CarSerializer(cars, many=True)

    if cars:
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@login_required
@api_view(['POST'])
def update_cars(request, pk):
    
    car= Car.objects.get(pk=pk)
    data= CarSerializer(instance=car, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_cars(request, pk):

    car= get_object_or_404(Car, pk=pk)
    car.delete()
    return Response(status=status.HTTP_202_ACCEPTED)




