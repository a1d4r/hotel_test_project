from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Hotel)
admin.site.register(RoomCategory)
admin.site.register(Room)
admin.site.register(Booking)
