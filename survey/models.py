from django.db import models

# Create your models here.
class SurveyUser(models.Model):
    name = models.CharField(max_length = 60)
    email = models.EmailField(max_length = 255)
    phone = models.CharField(max_length = 60)

    def __str__(self):
        return self.name

class Questions(models.Model):
    class CategoryChoices(models.TextChoices):
        WEB = 'Web'
        Android = 'Android'

    question = models.CharField(max_length = 200)
    category = models.CharField(max_length=90, choices=CategoryChoices.choices)

    def __str__(self):
        return self.question

class Answers(models.Model):
  
    class AnswerChoices(models.TextChoices):
        AGREE = 'Agree'
        DISAGREE = 'Disagree'

    question = models.ForeignKey(Questions, on_delete=models.DO_NOTHING)
    answer = models.BooleanField(default=True, blank=True)
    
    
class SurveyResults(models.Model):
    user = models.ForeignKey(SurveyUser, on_delete=models.DO_NOTHING)
    result = models.CharField(max_length=80)

    def __str__(self):
        return self.User
