from django.contrib import admin
from .models import post, Category, Aboutus

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
    search_fields = ('title', 'content')
    list_filter = ('category', 'created_at')

# Register your models here.

admin.site.register(post, PostAdmin)
admin.site.register(Category)
admin.site.register(Aboutus)

