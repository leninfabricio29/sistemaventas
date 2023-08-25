from django.db import models

# Create your models here.

CATEGORIA_CHOICES = (
    ("Desayunos","Desayunos"),
    ("Almuerzos","Almuerzos"),
    ("Bebidas","Bebidas"),
    ("Unico","Unico"),
)
    
    

class Producto(models.Model):
    nombre = models.CharField(max_length=40, blank=False)
    precio = models.DecimalField(max_length=4, max_digits=4, decimal_places=2)
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES, default="Seleccione")
    descripcion = models.CharField(max_length=120)

    def __str__(self):
        return self.nombre
    