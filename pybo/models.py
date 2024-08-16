from django.db import models


class Question(models.Model):
    subject=models.CharField(max_length=200)
    content=models.TextField()
    create_date=models.DateTimeField()
    def __str__(self):
        # id값대신 제목표시가능 self.subject __str__ 기본적으론 id를 표시함self.id(기본)
        return self.subject
    # Answer안에 외래키가있으므로
    # Question에서 answer_set으로
class Answer(models.Model):
    # Question의 역참조의 주체) question 필드로 작성한 질문들을 answer_set으로 여감조함 
    
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    content=models.TextField()
    create_date=models.DateTimeField()
    # related안쓰면 Question모델에서 역참조할때  는 answer_set으로 Answer을 역참조가능
    # question.answer로 접근가능 
    
# Create your models here.
