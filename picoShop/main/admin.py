from django.contrib import admin
from .models import Orders, token_storage

admin.site.register(Orders)
admin.site.register(token_storage)
