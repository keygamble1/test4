from django.contrib.auth.models import User
from django.db import models


class Question(models.Model):
    # user=1 question 다
    # 1이삭제시 다가 삭제되도록
    # 모델은형식
    modify_date=models.DateTimeField(null=True,blank=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='author_question')
    
    subject=models.CharField(max_length=200)
    content=models.TextField()
    create_date=models.DateTimeField()
    voter=models.ManyToManyField(User,related_name='voter_question')
    # 이미 User가 filed를 갖고있기땓문에 뭘더 할필요없음
    # 1 User가 이미 field가 있음
    
    def __str__(self):
        # id값대신 제목표시가능 self.subject __str__ 기본적으론 id를 표시함self.id(기본)
        return self.subject
    # Answer안에 외래키가있으므로
    # Question에서 answer_set으로
class Answer(models.Model):
    modify_date=models.DateTimeField(null=True,blank=True)
    # Question의 역참조의 주체) question 필드로 작성한 질문들을 answer_set으로 여감조함 
    # question삭제시 ansewr 다삭제
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='author_answer')
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    content=models.TextField()
    create_date=models.DateTimeField()
    voter=models.ManyToManyField(User,related_name='voter_answer')
    # related안쓰면 Question모델에서 역참조할때  는 answer_set으로 Answer을 역참조가능
    # question.answer로 접근가능 
    # git status 주루룩나오면 commit이 안된거
    # 빨간색이면 아직 add가안된거d
    # statge->commit 해야하는데
    # stage(add)->commit(commit)
    # 일단 status하고 빨이면 stage->commit
    # 노란색이면 commit 까지
    # status 아무것도안뜰때까지 해야함ee
# Create your models here.
