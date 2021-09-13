import uuid
from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.
class SurveyUser(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length = 60)
    email = models.EmailField(max_length = 255)
    phone = models.CharField(max_length = 60)
    
    def __str__(self):
        return self.name

class Questions(models.Model):
    class CategoryChoices(models.TextChoices):
        R = 'R'
        A = 'A'
        I = 'I'
        S = 'S'
        E = 'E'
        C = 'C'
    question = models.CharField(max_length = 200)
    category = models.CharField(max_length=90, choices=CategoryChoices.choices)
    img = models.ImageField(upload_to='photos/', blank=True)
    icon = models.FileField(upload_to='photos/', blank=True, null=True, validators=[FileExtensionValidator(['pdf', 'doc', 'svg', 'png'])])

    def __str__(self):
        return self.question


class SurveyResults(models.Model):
    survey_user = models.ForeignKey(SurveyUser, on_delete=models.DO_NOTHING, null=True)
    result = models.CharField(max_length=80, null=True)

    def __str__(self):
        return self.result
