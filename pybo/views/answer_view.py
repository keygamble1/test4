from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, redirect, render, resolve_url
from django.utils import timezone

from pybo.forms import AnswerForm, QuestionForm
from pybo.models import Answer, Question


@login_required(login_url='common:login')
def answer_create(request,question_id):
    # 대신 0,1,2,3,4,5,로 인덱스로 구별
    # 배열 [] [1,2,3,1,23]가능
    # () 튜플 인덱스있음 01,2,3,4, 중복되나 수정안됨 튜플
    # {}=셋과 딕셔너리 모두를 뜻함
    # set은 인덱스가 없어서 0,1,2,3,4,5 가안되기때문에 중복되면 구별이안됨
    # dictionary는 인덱스가없어도 인덱스대신 키값으로 구별하기땜에 값만 중복가능
    question=get_object_or_404(Question,pk=question_id)
    
    if request.method == "POST":
        form=AnswerForm(request.POST)
        
        if form.is_valid():
            answer=form.save(commit=False)
            answer.create_date=timezone.now()
            answer.question=question
            answer.author=request.user
            
            answer.save()
            return redirect('{}#answer_{}'.format(resolve_url('pybo:detail',question.id),answer.id))
        # url을 통해서 id를 조회가능하게만듬앵
            return redirect('pybo:detail',question.id)
    else:
        form=AnswerForm()
    context={'question':question,'form':form}
    # 여기에서 form은 answer의form quesiton과 별개라서 context에 넣어줌
    # form에서는 answer의 content만참조가가능하기에 question을따로 context에 넣어줘야함
    
    return render(request,'pybo/question_detail.html',context)
    # 레코드 얻음
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
            return redirect('{}#answer_{}'.format(resolve_url('pybo:detail',answer.question.id),answer.id))
    else:
        form=AnswerForm(instance=answer)
    context={'answer':answer,'form':form}
    return render(request,'pybo/answer_form.html',context)

@login_required(login_url="common:login")
def answer_delete(request,answer_id):
    answer=get_object_or_404(Answer,pk=answer_id)
    if request.user != answer.author:
        messages.error(request,'사용권한x')
    else:
        answer.delete()
    # 리다 딕 렌더 H
    return redirect('pybo:detail',answer.question.id)
    # 다 에서 1로 가서 id를 얻는다 
    # 일단 id부터 url에서 받아와함

@login_required(login_url="common:login")
def answer_vote(request,answer_id):
    answer=get_object_or_404(Answer,pk=answer_id)
    if request.user == answer.author:
        messages.error(request,'본인작성 x')
    else:
        # request.user는 쿼리셋 
        # answer.author 다대 일 일=쿼리셋
        answer.voter.add(request.user)
    return redirect('{}#answer_{}'.format(resolve_url('pybo:detail',answer.question.id),answer.id))
# html에서 #answer_{}로되어인거
