from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets


from .serializers import  VideojuegoSerializer
from .serializers import SalaSerializer
from .serializers import ComentarioSerializer
from .models import Videojuego
from .models import Sala
from .models import Comentario
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings



from profiles_api import models, serializers

from profiles_api.permissions import UpdateOwnProfile, UpdateOrDeletePost

from rest_framework import filters
from rest_framework import viewsets
from .forms impor OrderForm
from django.contrib.auth.models import User



class VideojuegoViewSet (viewsets.ModelViewSet):
    queryset = Videojuego.objects.all
    serializer_class = VideojuegoSerializer



class SalarViewSet (viewsets.ModelViewSet):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer

class ComentarioViewSet(viewsets.ModelViewSet):
        queryset = Comentario.objects.all()
        queryset2 = Sala.objects.all()
        serializer_class = ComentarioSerializer
        serializer_class2=SalaSerializer






    @api_view(["GET"])
    @csrf_exempt
    @permission_classes([IsAuthenticated])
    def welcome(request):
        content = {"message": "Welcome a mi libreria"}
        return JsonResponse(content)