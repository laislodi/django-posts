from django.contrib import admin
from .models import Post, Customer

admin.site.register([Post, Customer])
