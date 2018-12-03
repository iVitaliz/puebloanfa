from django.db import models

# Create your models here.
ESTADOS= (
    ('expulsado','expulsado'),
    ('disponible','disponible'),
)

class club(models.Model):    
    nombre_club = models.CharField(max_length=200)
    logo = models.ImageField()
    series = models.IntegerField()
    futbolistas_inscritos = models.IntegerField()
    pto_general = models.IntegerField()
    
def publish(self):
    self.save()

def __str__(self):
    return self.nombre_club


class jugador(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_jug = models.CharField(max_length=200)
    goles = models.IntegerField()
    tja_amarilla = models.IntegerField()
    tja_roja = models.IntegerField()
    estado = models.CharField(max_length=200,choices=ESTADOS)
    club = models.ForeignKey('club',on_delete=models.CASCADE)

def publish(self):
    self.save()

def __str__(self):
    return self.nombre_jug
