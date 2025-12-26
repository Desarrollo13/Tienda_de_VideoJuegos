from django.contrib import admin
from .models import Carrito,ItemCarrito

# Inline para mostrar las items dentro del carrito
class ItemCarritoInline(admin.TabularInline):
    model = ItemCarrito
    extra = 0 #no mostrar filas vacias adicionales
    readonly_fields=('subtotal',)#subtotal solo
#Admin del carrito
@admin.register(Carrito)
class CarritoAdmin(admin.ModelAdmin):
    list_display = ('usuario','total_items',
                  'total_precio','creado','actualizado')
    search_fields = ('usuario__username',)#Buscar carritos por nombre de usuario
    inlines = [ItemCarritoInline]
#Admin de los items(opcional,tambien accesible por separado)
@admin.register(ItemCarrito)
class ItemCarritoAdmin(admin.ModelAdmin):
    list_display=('carrito','juego','cantidad','subtotal')
    list_filter=('carrito',)
    search_fields=('juego__nombre',)  
    readonly_fields=('subtotal',)      
    