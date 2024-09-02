from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from common.forms import UserForm


# Create your views here.
def logout_view(request):
    logout(request)
    return redirect('index')

def signup(request):
    if request.method == "POST":
        form=UserForm(request.POST)
        # request.post도 class의 형태임
        if form.is_valid():
            form.save()
            # form의 필드값이 일치할경우 딕셔너리에 넣어버린다
            # 귀찮으니 form.errors로 통일하려고 form model형식으로 쓰는게 낫다
            username=form.cleaned_data.get('username')
            raw_password=form.cleaned_data.get('password1')
            user=authenticate(username=username,password=raw_password)
            login(request,user)
            return redirect('index')
    else:
        form=UserForm()
    return render(request,'common/signup.html',{'form':form})