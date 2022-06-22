from django.contrib import admin
from .models import Bikepost,Bikeimage,Biketable


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


class BikeImageAdmin(admin.ModelAdmin):
    list_display = ('id',  'image', 'alt')
    list_filter = ("id",)
    search_fields = ['id',]
    # prepopulated_fields = {'slug': ('title',)}


admin.site.register(Bikepost, PostAdmin)
admin.site.register(Bikeimage,BikeImageAdmin)
admin.site.register(Biketable)
