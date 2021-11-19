from django.shortcuts import render, redirect
from .models import Zona, Tour, User, Salida
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import datetime

from rest_framework import viewsets
from rest_framework import serializers

# Create your views here.
@login_required()
def index(request):
    """ Vista para atender la petición de la url / """
    # Obteniendo los datos mediantes consultas
    zonas = Zona.objects.all()
    tours = Tour.objects.all()

    # Se determina si el usuario pertenece o no al grupo editores
    #Aquí el usuario ya está logueado
    es_editor = request.user.groups.filter(name="editores").exists()

    return render(request, 'index.html', {"tours": tours, "zonas": zonas, "es_editor" : es_editor})

#Este login lo hicimos en un ejemplo anterior en el que no usábamos authenticate
"""def login(request):
    # Se definen los datos de un usuario válido
    usuario_valido = ("bedutravels", "bedutravels")

    # Si hay datos vía POST se procesan
    if request.method == "POST":
        # Se obtienen los datos del formulario
        usuario_form = (request.POST["username"],request.POST["password"])
        if usuario_form == usuario_valido:
            return redirect("index") #Redirige a la ruta que en urls.py de library tenemos con name "index"
        else:
            msg = "Datos incorrectos, intente de nuevo!"
    
    else:
        # Si no hay datos POST
        msg = ""

    return render(request, "registration/login.html", {"msg": msg})"""

#Login con authenticate
def login_user(request):
    """ Atiende las peticiones de GET /login/ """

     # Si hay datos vía POST se procesan
    if request.method == "POST":
        # Se obtienen los datos del formulario
        username = request.POST['username']
        password = request.POST['password']
        next = request.GET.get("next", "/")

        acceso = authenticate(username=username, password=password)

        if acceso is not None:
            # Se agregan datos al request para mantener activa la sesión
            login(request, acceso)
            return redirect(next)
        else:
            # Usuario malo
            msg = "Datos incorrectos"

    else:
        # Si no hay datos POST
        msg = ""

    return render(request, "registration/login.html", {"msg": msg, })

def logout_user(request):
    """ Atiende las peticiones de GET /logout/ """
    # Se cierra la sesión del usuario actual
    logout(request)

    return redirect('/login')

@login_required()
def eliminar_tour(request, idTour):
    """
    Atiende la petición GET
       /tour/eliminar/<int:idTour>/
    """
    # Se obtienen los objetos correspondientes a los id's
    tour = Tour.objects.get(pk=idTour)

    # Se elimina el tour
    tour.delete()

    #Retorna a la página de inicio
    return redirect("/")

class UserSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializador para atender las conversiones para User """
    class Meta:
        # Se define sobre que modelo actua
        model = User
        # Se definen los campos a incluir
        fields = ('id','name', 'last_name', 'email', 'birthday', 'genre', 'key', 'type')

class UserViewSet(viewsets.ModelViewSet):
    # Se define el conjunto de datos sobre el que va a operar la vista,
    # en este caso sobre todos los users disponibles.
    queryset = User.objects.all().order_by('id')
    # Se define el Serializador encargado de transformar la peticiones
    # en formato JSON a objetos de Django y de Django a JSON.
    serializer_class = UserSerializer

class SalidaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Salida
        fields = ('fechaInicio', 'fechaFin', 'asientos', 'precio', 'tour')

class TourSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializador para atender las conversiones para Tour """

    salidas = SalidaSerializer(many=True, read_only=True) #Un tour tiene muchas salidas

    class Meta:
        model = Tour
        fields = ('id', 'nombre', 'slug', 'operador', 'tipoDeTour',
         'descripcion', 'img', 'pais', 'zonaSalida', 'zonaLlegada', 'salidas')

class ZonaSerializer(serializers.HyperlinkedModelSerializer):
    """Serializador para atender las conversiones para Zona"""

    # Se define la relación (uno a muchos) de una zona y sus tours relacionados
    tours = TourSerializer(many=True, read_only=True) #Una zona tiene muchos tours

    class Meta:
        model = Zona
        #fields = ('id', 'nombre', 'descripcion', 'longitud', 'latitud') #Sin considerar los tours relacinados a la zona
        fields = ('id', 'nombre', 'descripcion', 'longitud', 'latitud', 'tours', 'tours_salida', 'tours_llegada') #Considerando los tours relacinados a la zona... Los nombres tours_salida y tours_llegada están definidos en el modelo Tour

class ZonaViewSet(viewsets.ModelViewSet):
    """API que permite realizar operaciones en la tabla Zona"""
    queryset = Zona.objects.all().order_by('id')
     # Se define el Serializador encargado de transformar la peticiones en formato JSON a objetos de Django y de Django a JSON.
    serializer_class = ZonaSerializer

class TourViewSet(viewsets.ModelViewSet):
   """API que permite realizar operaciones en la tabla Tour"""
   queryset = Tour.objects.all().order_by('id')
   serializer_class = TourSerializer

class SalidaViewSet(viewsets.ModelViewSet):
    """API que permite realizar operaciones en la tabla Salida"""
    queryset = Salida.objects.all().order_by('id')
    serializer_class = SalidaSerializer





