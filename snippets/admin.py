from django.contrib import admin
from rest_framework.authtoken.admin import TokenAdmin
from snippets import models

admin.site.register(models.Snippet)
