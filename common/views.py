from django.contrib.auth import logout
from django.shortcuts import redirect, render


# Create your views here.
def logout_view(request):
    logout(request)
    return redirect('index')

def signup(request):
    pass