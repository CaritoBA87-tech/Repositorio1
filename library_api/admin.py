from django.contrib import admin
from .models import User, Zona, Tour, Salida #Importamos los modelos

# Register your models here.
admin.site.register(Zona)

# Personalizamos la vista de la tabla User en la página de admin
class UserAdmin(admin.ModelAdmin):
    # Se sobre escribe lo que hace __str__
    list_display = ("id", "name", "last_name", "email", "birthday",)
        #Especificamos los campos a mostrar

admin.site.register(User, UserAdmin)

# Personalizamos la vista de la tabla Tour en la página de admin
class TourAdmin(admin.ModelAdmin):
    # Se sobre escribe lo que hace __str__
    list_display = ("id", "nombre", "slug", "operador", "tipoDeTour",
        "descripcion", "pais", "zonaSalida", "zonaLlegada")

admin.site.register(Tour, TourAdmin)

# Personalizamos la vista de la tabla Salida en la página de admin
class SalidaAdmin(admin.ModelAdmin):
    # Se sobre escribe lo que hace __str__
    list_display = ("id", "fechaInicio", "fechaFin", "asientos", "precio", "tour")

admin.site.register(Salida, SalidaAdmin)