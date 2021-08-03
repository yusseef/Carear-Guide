from django.contrib import admin
from .models import SurveyUser, Questions, SurveyResults, Answers
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email']

class QuestionsAdmin(admin.ModelAdmin):
    list_display = ['question']

class SurveyResultsAdmin(admin.ModelAdmin):
    list_display = ['user', 'result']

class AnswersAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer']

admin.site.register(SurveyUser, UserAdmin)
admin.site.register(Questions, QuestionsAdmin)
admin.site.register(SurveyResults, SurveyResultsAdmin)
admin.site.register(Answers, AnswersAdmin)