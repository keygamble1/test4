from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from pybo.forms import AnswerForm, QuestionForm
from pybo.models import Answer, Question


# Create your views here.
def index(request):
    page=request.GET.get('page','1')
    kw=request.GET.get('kw','')
    # 기본값 0
    # request.GET은 pybo/?page=3이라면 딕셔너리 {'page','3'} 과같이 반환함
    # {'page','3'}.get('page','1') ㅣ라는뜻?
    # page키가 존재할경우 3을 반환,없을경우는 1을 기본적으로 반환한다는뜻
    
    
    # objects 를 한순간 모델에해당하는 list다 불러오는거
    question_list=Question.objects.order_by('-create_date')
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 제목 검색
            Q(content__icontains=kw) |  # 내용 검색
            Q(answer__content__icontains=kw) |  # 답변 내용 검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이 검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이 검색
        ).distinct()
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
    context={'question_list':page_obj,'page':page,'kw':kw}
    # 전달안해주면 html에서 뭘가져오는지모름
    
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
    