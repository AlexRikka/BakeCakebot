from django.contrib import admin


from .models import Cake, Client

admin.site.register(Cake)
admin.site.register(Client)