from django.contrib import admin
from .models import *
admin.site.register(Review)
admin.site.register(Shop)
class BookAdmin(admin.ModelAdmin):
    search_fields = ('name', 'author')
    exclude = ('pages',)
admin.site.register(Book, BookAdmin)
