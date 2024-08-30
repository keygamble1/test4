from django import forms

from pybo.models import Answer, Question

# forms.model models.model

# models.model forms.modelform
# QuestionForm은 Question의 모델과 연결된 폼이고
# Question모델의 subject,content를 사용한다고 정의한것
class QuestionForm(forms.ModelForm):
    class Meta:
        # forms.ModelForm에서 model,fields,labels를 불러오는것
        model = Question
        fields = ['subject','content']
        # widgets={
            
        #     'subject':forms.TextInput(attrs={'class':'form-control'}),
        #     'content':forms.TextInput(attrs={'class':'form-control','rows':10}),
        # }
        labels={
            'subject':'제목',
            'content':'내용',
        }
        
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels={
            'content':'답변내용',
        }