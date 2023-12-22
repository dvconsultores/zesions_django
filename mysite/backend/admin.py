from django.contrib import admin
from django.apps import apps
from .models import *

myapp = apps.get_app_config('backend')
for model in myapp.get_models():
    admin.site.register(model)
