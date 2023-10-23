from django.contrib import admin

# Register your models here.
from .models import Tasks,Phrase

admin.site.register(Tasks)
admin.site.register(Phrase)