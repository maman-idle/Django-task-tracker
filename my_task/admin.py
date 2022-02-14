from django.contrib import admin
from .models import MyCustomUser, Task


admin.site.register(MyCustomUser)
admin.site.register(Task)
