from django.shortcuts import render ,redirect
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm,LoginForm
from django.contrib import messages

# Create your views here.
def registro_view(request):
    if request.method=='POST':
        form=RegistroForm(request.POST)
        if form.is_valid():
            usuario= form.save()
            login(request,usuario)
            messages.success(request, "Registro completado correctamente. ")
            return redirect('home')
    else:
        form=RegistroForm()
    return render(request,'usuarios/registro.html',{'form':form})        

# vista de login
def login_view(request):
    if request.method =='POST':
        form=LoginForm(request, data=request.POST)
        if form.is_valid():
            usuario= form.get_user()
            login(request,usuario)
            messages.success(request, "Inicio de sesión correcto. ")
            return redirect('home')
        else:
            # mostar errores generales por consola para debug
            print(form.errors)
            messages.error(request,"Usuarios o contraseña incorrectos.")
    else:
        form=LoginForm()
    return render(request,'usuarios/login.html',{'form':form})
# vista de cerrar sesion logout
def logout_view(request):
    logout(request)
    messages.info(request, "Has cerrado sesion correctamente. ")
    return redirect('login')
@login_required
def perfil_view(request):
    return render(request,'usuarios/perfil.html')
            
