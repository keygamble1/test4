

from django.urls import path

from . import views
from .views import answer_view, base_views, question_view

# 별칭중복 고려해서 app_name써줌dd
app_name='pybo'


urlpatterns = [
    #base_view.py
    path('',base_views.index,name='index'),
    path('<int:question_id>/',base_views.detail,name='detail'),
    
    
    # 맨끝에 /페이지를 못찾음
    #question_view.py
   
    path('question/create',question_view.question_create,name='question_create'),
    path('question/modfiy/<int:question_id>/',question_view.question_modify,name='question_modify'),
    path('question/delete/<int:question_id>/',question_view.question_delete,name='question_delete'),
    path('quesiton/vote/<int:question_id>/',question_view.question_vote,name='question_vote'),
    #answer_view.py
    path('answer/create/<int:question_id>/',answer_view.answer_create,name='answer_create'),
    path('answer/modify/<int:answer_id>/',answer_view.answer_modify,name='answer_modify'),
    path('answer/delete/<int:answer_id>/',answer_view.answer_delete,name='answer_delete'),
    path('answer/vote/<int:answer_id>/',answer_view.answer_vote,name='answer_vote'),
    
    # 딕셔너리 int형의 question_id를 받는것
]
