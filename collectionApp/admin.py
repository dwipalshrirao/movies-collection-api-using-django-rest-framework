from django.contrib import admin

# Register your models here.


from collectionApp.models import Movies, Genres,Collection

admin.site.register(Movies)
admin.site.register(Genres)
admin.site.register(Collection)