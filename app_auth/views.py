from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import*


# Create your views here.

def login_blog(request):
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            pwd=form.cleaned_data['pwd']
            user=authenticate(username=username,password=pwd)
            if user is not None:
                #si la connexion s'est bien passer
                login(request,user)
                return redirect('home')
            else:
                #authenticate retourne une erreur de connexion
                messages.error(request,"Mot de passe et/ou nom d'utilisateur invalide, veillez ressayer svp")
                return render(request,'login.html',{"form":form})
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class']+=' is-invalid'
            return render(request,'login.html',{"form":form})

    else:
        form=LoginForm()
        return render(request,"login.html",{"form":form})

def register(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            pwd=form.cleaned_data['pwd']
            user=User.objects.create_user(username=username,password=pwd)
            if user is not None:
                return redirect("login-blog")
            else:
                messages.error(request,"Creation de compte echouer reessayer.")
                return render(request,'register.html',{"form":form})
        else:
            return render(request,'register.html',{"form":form})
        return render(request,'register.html')
    form=RegisterForm()
    return render(request,"register.html",{"form":form})

def logout_user(request):
    logout(request)
    #la page a rendre quand l'utilisateur a ete deconnecter
    return redirect("home")




