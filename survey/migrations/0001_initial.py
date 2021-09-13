# Generated by Django 3.2.5 on 2021-09-13 11:36

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('R', 'R'), ('A', 'A'), ('I', 'I'), ('S', 'S'), ('E', 'E'), ('C', 'C')], max_length=90)),
                ('img', models.ImageField(blank=True, upload_to='photos/')),
                ('icon', models.FileField(blank=True, null=True, upload_to='photos/', validators=[django.core.validators.FileExtensionValidator(['pdf', 'doc', 'svg', 'png'])])),
            ],
        ),
        migrations.CreateModel(
            name='SurveyUser',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=255)),
                ('phone', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='SurveyResults',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.CharField(max_length=80, null=True)),
                ('survey_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='survey.surveyuser')),
            ],
        ),
    ]
