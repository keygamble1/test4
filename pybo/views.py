from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from pybo.forms import AnswerForm, QuestionForm
from pybo.models import Question


# Create your views here.
def index(request):
    page=request.GET.get('page','1')
    # request.GET은 pybo/?page=3이라면 딕셔너리 {'page','3'} 과같이 반환함
    # {'page','3'}.get('page','1') ㅣ라는뜻?
    # page키가 존재할경우 3을 반환,없을경우는 1을 기본적으로 반환한다는뜻
    
    
    # objects 를 한순간 모델에해당하는 list다 불러오는거
    question_list=Question.objects.order_by('-create_date')
    paginator=Paginator(question_list,'10')
    # paginator로인해서 ?page= 을 사용가능
    
    # 페이지당 보여줄갯수
    # paginator 갯수이긴한데 어떤페이지인지 확인후
    # page_obj에 넣는다
    page_obj=paginator.get_page(page)
    
    # 데이터 전체를 조회하지않고 해당페이지만 조회하도록 쿼리가변경됨
    # paginator로 묶어서 html에서 메서드쓰게하는용도
    # 현재 페이지를 get_page에 넣는다
    # question_list.start_index
    # forloop.counter
    # question_list.paginator.count
    # question_list.has_previous
    # question_list.has_next
    # question_list.paginator.page_range
    # question_list.number==현재페이지
    # question_list.next_page_number
    # question_list.previous_page_number
    context={'question_list':page_obj}

    
    # basedir/templates/를 했기때문에 pybo/쓰면됨
    return render(request,'pybo/question_list.html',context)
    # s내림차순은 앞에 -를 붙여야함 
# as_로시작하는건 객체나 클래스의 데이터를 다른형식으로 변환 혹은 
# 객체의 동작을 특정방식으로 호출할수있께변환
# as_p이건 폼의 필드를 html형식으로변환 form.as_p 폼을 html p
# as_view 클래스뷰를 함수형뷰로 변환하여 url패턴에 매핑가능하게함 url설정에서 view를 호출함
# auth_views.loginview.as_view auth 클래스뷰를 함수형뷰 즉 url설정에서 쓸수있게만들어버림 url에서 사용
def detail(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    context={'question':question}
    return render(request,'pybo/question_detail.html',context)
    # filed는 list로 0,1로 구분가능
    
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
            return redirect('pybo:detail',question.id)
    else:
        return HttpResponseNotAllowed('only post is possible.')
    context={'question':question,'form':form}
    # 여기에서 form은 answer의form quesiton과 별개라서 context에 넣어줌
    # form에서는 answer의 content만참조가가능하기에 question을따로 context에 넣어줘야함
    
    return render(request,'pybo/question_detail.html',context)
    # 레코드 얻음
    # queestion.answer_set역참조시 question은 자동으로 answer필드로 들어감
    # create,add,set,remove등 다 알아서 question를 역참조로 필드에 자동등록된다
    # request.POST는 QUERTDICT 형식임
    # querydict=request.post,request.get 주로 http get post형태
    # queryset=django orm 에서 쿼리작성후 실행하는데씀
    # querydict=get(key,value),key없으면 default,getlist,.key,.items
    # .lists .copy .update(date) 추가
    # queyset 객체 .all .filter, .gxclude .get .count .values .values_list ,.order_by.dicntict()
    # question.answer_set.create(content=request.POST.get('content'),create_date=timezone.now())
    
    # content에 의 키값(name) 을찾아서 value를 가져와라
    # 모델_set 모델셋
    # login_url안쓰면 account라는 이상한대로가버림
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