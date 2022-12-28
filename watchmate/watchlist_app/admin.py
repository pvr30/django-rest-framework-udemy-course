from django.contrib import admin
# from .models import Movie

# Register your models here.
# admin.site.register(Movie)

from .models import WatchList, StreamPlatform, Review

admin.site.register(WatchList)
admin.site.register(StreamPlatform)
admin.site.register(Review)
