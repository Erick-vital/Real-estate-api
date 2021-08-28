from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import InmuebleSerializer
from .models import Inmueble

# Create your views here.

def index(request):
    return render(request, 'index.html')

# 'api_view' escoje los metodos HTTP a usar en esta vista
@api_view(['GET', 'POST'])
def inmueble_list(request):
    """
    Lista todos los inmuebles y podemos enviar un 
    formulario(POST) para crear un nuevo objeto
    """
    if request.method == 'GET':
        inmuebles = Inmueble.objects.all()
        serializer = InmuebleSerializer(inmuebles, many=True)
        return Response(serializer.data)

    # Para rellenar el formulario tenemos que enviar un objeto JSON con los datos
    if request.method == 'POST':
        serializer = InmuebleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)       
    
@api_view(['GET'])
def detail_inmueble(request, pk):
    """
    Muestra unicamente el objeto seleccionado 'pk'
    """
    inmueble = Inmueble.objects.get(id=pk)
    serializer = InmuebleSerializer(inmueble, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def update_inmueble(request, pk):
    """
    Actualiza un objeto, llena el formulario actualizando el objeto json
    """
    inmueble = Inmueble.objects.get(id=pk)
    serializer = InmuebleSerializer(instance=inmueble, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
def delete_inmueble(request, pk):
    inmueble = Inmueble.objects.get(id=pk)
    inmueble.delete()

    return Response('Deleted', status=status.HTTP_200_OK)