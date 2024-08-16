from django.test import TestCase
from django.utils import timezone

from pybo.models import Answer, Question


# Create your tests here.
class MymodelTest(TestCase):
    def test(self):
        for i in range(300):
            q = Question(subject='테스트 데이터입니다:[%03d]' % i, content='내용무', create_date=timezone.now())
            q.save()
        # q=Question(subject='pybo가 무엇인가?',content='pybo에 대해 알고싶음',create_date=timezone.now())
        # q.save()
        # print(q.id)
        # q = Question(subject='장고 모델 질문입니다.', content='id는 자동으로 생성되나요?', create_date=timezone.now())
        # q.save()
        # print(q.id)
        # # objects는 쿼리셋
        # print(Question.objects.all())
        # print(Question.objects.filter(id=1))
        # # filter는 QuesrySet이 리턴 조건에 해당하는 데이어틀 모두 리턴해버림
        # # 모델에 메서드가 추가되력ㅇ우에는 migrations를 할필요없음, 속성이 변경될때만 쓰지 값이 넣어질경우는 무관
        # print(Question.objects.get(id=1))
        # # id는 유일값이기때무넹 get으로 조회가능 
        # print(Question.objects.filter(subject__contains='장고'))
        # q=Question.objects.get(id=2)
        # print(q)
        # q.subject='Django Model Question'
        # q.save()
        # # q라는 객체 Question.objects=쿼리셋 .get하는순간 객체로변환
        # # 그리고나서 이객체를 .save()나 .delete()를해서 데이터베이스에서
        # # 작업을하면 이순간 모델이되어버림
        # # 모델에서는 id
        
        
        # print(q)
        # q=Question.objects.get(id=1)
        # q.delete()
        # print(Question.objects.all())
        # print('all')
        # q=Question.objects.get(id=2)
        # a= Answer(question=q,content='네 자동생성됨',create_date=timezone.now())
        # a.save()
        # print(a.id)
        # a=Answer.objects.get(id=1)
        # print(a.question)
        # print(q.answer_set.all())
        # filter안에는 id인값을넣는것