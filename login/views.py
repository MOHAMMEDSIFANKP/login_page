from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models  import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from .models import cameras

# Create your views here.
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def index(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        use=request.POST['user']
        paw=request.POST['password']
        user=auth.authenticate(username=use,password=paw)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    return render(request,'index.html')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url='login')
def home(request):
    dict_docs = {
        'photos': cameras.objects.all()
    }
    return render(request,'home.html',dict_docs)

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')
