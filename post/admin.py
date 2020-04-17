from django.contrib import admin

# Register your models here.
from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'desc']

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)