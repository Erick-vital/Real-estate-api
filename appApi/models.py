from django.db import models

# Create your models here.

class Vendedor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    descripcion = models.TextField()
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Inmueble(models.Model):
    TIPO_DE_INMUEBLE = [
        ('CA', 'Casa'),
        ('CO', 'Comercial'),
        ('DE', 'Departamento'),
        ('OF', 'Oficinas'),
        ('TE', 'Terreno / Lote'),
    ]

    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    inmueble = models.CharField(max_length=20, choices=TIPO_DE_INMUEBLE)
    ubicacion = models.CharField(max_length=100)
    precio = models.IntegerField()
    metros_cuadrados = models.IntegerField()
    metros_cuadrados_construidos = models.IntegerField(default=0, null=True)
    banos = models.IntegerField(default=0, null=True)
    cuartos = models.IntegerField(default=0, null=True)

    def __str__(self):
        texto = '{inmueble} en {ubicacion}'

        return texto.format(inmueble=self.inmueble, ubicacion=self.ubicacion)