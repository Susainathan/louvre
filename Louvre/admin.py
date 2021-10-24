from django.contrib import admin
from .models import Registeron

class registerAdmin(admin.ModelAdmin):
    list_display=('Name','Email','Age','Gender','City','Country','Username','Password')

admin.site.register(Registeron,registerAdmin)