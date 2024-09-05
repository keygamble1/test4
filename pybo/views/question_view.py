from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from pybo.forms import AnswerForm, QuestionForm
from pybo.models import Answer, Question


@login_required(login_url='common:login')
def question_create(request):
    if request.method == "POST":
        form=QuestionForm(request.POST)
        if form.is_valid():
            question=form.save(commit=False)
            question.create_date=timezone.now()
            question.author=request.user
            question.save()
            return redirect('pybo:index') 
        # form에 들어갈 model만 forms.py에넣고 그외에는 views에서 자동처리하게만듬
        # post의 들어갈데이터는 form에다가  
        
    else:
        
        form=QuestionForm()
        
    context={"form":form}
    # render는 html 폴더에서
    # redirect는 url로 웹브라우저에서 딕셔너리로
    # request받는이유는 전에 썼던 html에서 변수를 그대로 적용허기위해서쓰는것
    # redirect는 그냥 url인거고
    return render(request,'pybo/question_form.html',context)

@login_required(login_url='common:login')
def question_modify(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    if request.user != question.author:
        messages.error(request,'수정권한 x')
        return redirect('pybo:detail',question.id)
    if request.method == "POST":
        # form은 비우거나 request.POST를 하나 넣거나
        # request.POST,indtance=question 이런식으로 모델넣어줌
        # instance는 채워주는용도 안채
        #  inctance는 값을 표시해주는거라고 이해
        # request.POST는 덮어씌우라는것
        # QuestionForm(덮어씌우기 request.POST,원래 있는거 표시하기 inctance)
        # qUESTIONfORM(덮어씌우기,"")라고봐야함
        # QustionForm(request.post,'') 기본상태라고보자
        form=QuestionForm(request.POST,instance=question)
        if form.is_valid():
            question=form.save(commit=False)
            question.modify_date=timezone.now()
            question.save()
            return redirect('pybo:detail',question.id)
    else:
        # 값을 불러오지말고 표시만하라 get일경우?
        form=QuestionForm(instance=question)
    context={'form':form}
    return render(request,'pybo/question_form.html',context)
    # html 경로이기때문에 / 라 써줌 

@login_required(login_url="common:login")
def question_delete(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    if request.user != question.author:
        messages.error(request,'삭제권한이 없음')
        return redirect('pybo:detail',question.id)
    question.delete()
    return redirect('pybo:index')

@login_required(login_url='common:login')
def answer_modify(request,answer_id):
    answer=get_object_or_404(Answer,pk=answer_id)
    if request.user != answer.author:
        messages.error(request,'수정권한x')
        return redirect('pybo:detail',answer.question.id)
    if request.method == "POST":
        form=AnswerForm(request.POST,instance=answer)
        if form.is_valid():
            answer=form.save(commit=False)
            # 아직전체  save하지말고 되어있는것만 save
            answer.modify_date=timezone.now()
            answer.save()
            return redirect('pybo:detail',answer.question.id) 
    else:
        form=AnswerForm(instance=answer)
    context={'answer':answer,'form':form}
    return render(request,'pybo/answer_form.html',context)
@login_required(login_url='common:login')
def question_vote(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    if request.user == question.author:
        messages.error(request,'본인작성 x')
    else:
        question.voter.add(request.user)
    return redirect('pybo:detail',question.id)
