from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# contribute 원인 .인증. forms.py 는 form과 models,field가 필요
# 그래서 forms. usercreateForm 과 models인 user를 불러옴
class UserForm(UserCreationForm):
    # 모델은 데이터베이스 구조를 정의하고, 
    # 폼은 사용자 입력을 처리하는 데 사용됩니다.
    # 필드를 안할경우 error가 안나와서 필드를 빼먹고 form에 넣어서 경고가
    # 되는지도모르기땜에 왠만하면 이렇게하는 형식이 좋다
    email=forms.EmailField(label="이메일")
    class Meta:
        model = User
        fields = ["username","password1","password2","email"]

# d
# Form을 부르는거니까 일단 ,model과 field가 있어야함
