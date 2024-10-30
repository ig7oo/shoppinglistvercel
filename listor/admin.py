from django.contrib import admin
from .models import List, Item

# Register your models here.

class ItemInline(admin.TabularInline):
    model = Item
    extra = 1

class ListAdmin(admin.ModelAdmin):
        inlines = [ItemInline]

admin.site.register(List, ListAdmin)