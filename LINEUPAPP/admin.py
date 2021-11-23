from django.contrib import admin
from .models import Lineupapp, Avaliacao

@admin.register(Lineupapp)
class LineupAdmin(admin.ModelAdmin):
    list_display = ('título','url', 'criacao', 'atualizacao','ativo')

@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('lineup','nome', 'email', 'avaliacao', 'criacao', 'atualizacao', 'ativo')