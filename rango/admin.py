from django.contrib import admin
from rango.models import Category, Page
from django.utils.html import format_html

# Register your models here.

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

admin.site.register(Category)
admin.site.register(Page, PageAdmin)



