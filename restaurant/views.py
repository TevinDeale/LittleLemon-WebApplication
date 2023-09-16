from django.shortcuts import render
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Menu
from .serializers import MenuSerializer
from .forms import MenuForm

from rest_framework import generics

# Create your views here.
def home(request):
    return render(request, 'index.html', {})
# Menu API Views       
class MenuList(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({'message': 'Menu item created successfully'}, status=status.HTTP_201_CREATED)

class SingleMenuItem(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer