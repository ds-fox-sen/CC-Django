from django.contrib import admin

# Register your models here.

from learning_logs.models import Topic

# Manage our model through the admin site.
admin.site.register(Topic)
