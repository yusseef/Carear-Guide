from django.contrib import admin
from .models import SurveyUser, Questions, SurveyResults
from import_export.admin import ExportActionMixin
# Register your models here.
class UserAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone']

class QuestionsAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ['id', 'question', 'category']

class SurveyResultsAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ['survey_user', 'result']
    list_filter = ['survey_user', 'result']
    search_fields = ['survey_user__email',]
    
    

admin.site.register(SurveyUser, UserAdmin)
admin.site.register(Questions, QuestionsAdmin)
admin.site.register(SurveyResults, SurveyResultsAdmin)
