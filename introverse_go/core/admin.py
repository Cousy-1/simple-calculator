from django.contrib import admin
from .models import Product

admin.site.register(Product)
from django.contrib import admin

from .models import Product, ContactMessage, Feature, UserProfile, AdminSettings


# Register your models here.
