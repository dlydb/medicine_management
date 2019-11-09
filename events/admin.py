from django.contrib import admin
from . import models

admin.site.register(models.Medication)
admin.site.register(models.Canister)
admin.site.register(models.Schedule)