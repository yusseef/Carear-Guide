from django.contrib import admin
from .models import SurveyUser, Questions, SurveyResults
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email']

class QuestionsAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'category']

class SurveyResultsAdmin(admin.ModelAdmin):
    list_display = ['survey_user', 'result']

admin.site.register(SurveyUser, UserAdmin)
admin.site.register(Questions, QuestionsAdmin)
admin.site.register(SurveyResults, SurveyResultsAdmin)
