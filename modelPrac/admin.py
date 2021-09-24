from django.contrib import admin
from .models import Child, Musician, Album, Concert

# Register your models here.
admin.site.register(Child)
admin.site.register(Musician)
admin.site.register(Album)
admin.site.register(Concert)