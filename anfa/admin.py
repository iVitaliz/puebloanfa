from django.contrib import admin
from .models import club
from .models import jugador

# Register your models here.
admin.site.register(club)
admin.site.register(jugador)