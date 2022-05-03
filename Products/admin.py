from django.contrib import admin

# Register your models here.
from .models import Vendor, Product
from django.db.models import F


admin.site.register(Vendor)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['get_diff', 'get_name', 'description', 'price', 'current_volume', 'min_available_volume', 'vendor']
    
    def get_queryset(self, request):
        qs = super(ProductAdmin, self).get_queryset(request)
        qs = qs.annotate(diff = F('current_volume') - F('min_available_volume'))
        return qs

    
    def get_diff(self, obj):
        return obj.diff
    
    def get_name(self, obj):
        return obj.name

    get_diff.admin_order_field = 'diff'
    
    get_name.short_description = 'Имя'
    get_diff.short_description = 'Важность закупки'