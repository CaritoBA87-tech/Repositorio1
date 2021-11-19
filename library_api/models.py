from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=80, null=True, blank=True) #El campo en la BD puede ser null y el campo en el formulario puede quedar en blanco
    email = models.EmailField()
    birthday = models.DateField(null=True, blank=True)

    GENERO = [("H", "Hombre"),("M", "Mujer")]

    genre = models.CharField(max_length=1, choices=GENERO)
    key = models.CharField(max_length=40, null=True, blank=True)
    type = models.CharField(max_length=45, null=True, blank=True) 

class Zona(models.Model):
    """ Define la tabla Zona """
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=256, null=True, blank=True)
    latitud = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True)
    longitud = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True)

    #Esta función nos sirve para mostrar un texto legible para los registros de la tabla Zona desde el admin
    def __str__(self):
        """ Se define la representación en str para Zona """
        return "{}".format(self.nombre) 

class Tour(models.Model):
    """ Define la tabla Tour """
    nombre = models.CharField(max_length=145)
    slug = models.CharField(max_length=45, null=True, blank=True)
    operador = models.CharField(max_length=45, null=True, blank=True)
    tipoDeTour = models.CharField(max_length=45, null=True, blank=True)
    descripcion = models.CharField(max_length=256)
    img = models.CharField(max_length=256, null=True, blank=True)
    pais = models.CharField(max_length=45, null=True, blank=True)
    zonaSalida = models.ForeignKey(Zona, on_delete=models.SET_NULL, null=True,
        blank=True, related_name="tours_salida")
    zonaLlegada = models.ForeignKey(Zona, on_delete=models.SET_NULL, null=True,
        blank=True, related_name="tours_llegada")

    #Esta función nos sirve para mostrar un texto legible para los registros de la tabla Tour desde el admin
    def __str__(self):
        return "{}".format(self.nombre)

class Salida(models.Model):
    """ Define la tabla Salida """
    fechaInicio = models.DateField()
    fechaFin = models.DateField()
    asientos = models.PositiveSmallIntegerField(null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    tour = models.ForeignKey(Tour, related_name="salidas", on_delete=models.CASCADE)
    #Con on_delete=models.CASCADE indicamos que si se elimina el tour se va a eliminar también la salida

    #Esta función nos sirve para mostrar un texto legible para los registros de la tabla Salida desde el admin
    def __str__(self):
        return "{} ({}, {})".format(self.tour, self.fechaInicio, self.fechaFin)