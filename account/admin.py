from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models
from .models import CustomUser

admin.site.register(CustomUser)  # Register your custom user model
