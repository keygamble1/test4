from django.contrib.auth import views as auth_view
from django.urls import path, re_path

app_name = 'common'

urlpatterns = [
    path('login',auth_view.LoginView.as_view(template_name='common/login.html'),name='login')
    # auth_view에서 모델을 다 만들었기때문에 views에서 따로 할건없음
    
]