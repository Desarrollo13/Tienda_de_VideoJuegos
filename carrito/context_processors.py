from .models import Carrito


# es una fucnion que inyecta un contador en forma automatica
def carrito_total(request):
    total_items =0
    if request.user.is_authenticated:
        carrito = Carrito.objects.filter(usuario=request.user).first()
        if carrito:
            total_items= carrito.total_items()
    return{'carrito_total_items':total_items}        