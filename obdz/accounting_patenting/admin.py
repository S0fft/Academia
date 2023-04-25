from django.contrib import admin
from . import models


admin.site.register(models.Owner)
admin.site.register(models.Document)
admin.site.register(models.CopyrightObject)
admin.site.register(models.MainPatent)
