from django.contrib import admin
from .models import Category, RoomSize,Room,User,Deal,Employee

admin.site.register(Category)
admin.site.register(Room)
admin.site.register(RoomSize)
admin.site.register(Employee)
admin.site.register(User)
admin.site.register(Deal)

# Register your models here.
