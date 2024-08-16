

from django.urls import path

from . import views

# 별칭중복 고려해서 app_name써줌
app_name='pybo'


urlpatterns = [
    path('',views.index,name='index'),
    path('<int:question_id>/',views.detail,name='detail'),
    # 맨끝에 /페이지를 못찾음
    path('answer/create/<int:question_id>/',views.answer_create,name='answer_create'),
    path('question/create',views.question_create,name='question_create'),
    # 딕셔너리 int형의 question_id를 받는것
]
