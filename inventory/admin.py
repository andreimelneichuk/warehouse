
# Register your models here.
from django.contrib import admin
from .models import Stock, Category, Equipment

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    search_fields = ['name', 'location']
    list_filter = ['location']
    list_display = ['name', 'location', 'created_at']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'created_at']

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    search_fields = ['name', 'serial_number']
    list_filter = ['category', 'stock']
    list_display = ['name', 'serial_number', 'stock', 'category', 'created_at']