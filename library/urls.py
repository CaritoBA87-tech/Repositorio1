"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from library_api import views
from django.contrib.auth import views as auth_views

from rest_framework import routers

from graphene_django.views import GraphQLView
from library_api import schema #Este schema.py lo creamos nosotros

# Agregando rutas para django rest
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet) #http://127.0.0.1:8000/api/users/
router.register(r'zonas', views.ZonaViewSet) #http://127.0.0.1:8000/api/zonas/
router.register(r'tours', views.TourViewSet) #http://127.0.0.1:8000/api/tours/
router.register(r'salidas', views.SalidaViewSet) #http://127.0.0.1:8000/api/salidas/

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    #path("login/", views.login, name="login"), #Login sin usar authenticate
    #path("login/", views.login_user, name="login"), #Login con vista de función
    path("login/", auth_views.LoginView.as_view(template_name="registration/login2.html"), name="login_user"), #Este es un login built in de Django
    #path('logout/', views.logout_user, name="logout_user"), #Logout con vista de función
    path("logout/", auth_views.LogoutView.as_view(next_page="/login/"), name="logout"), #Este es un logout built in de Django
    path("tour/eliminar/<int:idTour>/",views.eliminar_tour, name="eliminar_tour"),

    #Rutas del API
    path("api/", include(router.urls)), 
    path("api/auth/", include("rest_framework.urls", namespace="rest_framework")),

    #Rutas para graphene
    path("graphql", GraphQLView.as_view(graphiql=True, schema=schema.schema))

]
