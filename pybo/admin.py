from django.contrib import admin

from pybo.models import Question


# admin에넣고싶으면 admin.site.resgister(Quetion)해줌
# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    search_fields=['subject']
admin.site.register(Question,QuestionAdmin)


