from django.contrib import admin
from django.db import models

from .models import Itinerary, Location, Comment, Photo

admin.site.register(Itinerary)
admin.site.register(Location)
admin.site.register(Comment)
admin.site.register(Photo)

