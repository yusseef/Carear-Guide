# Generated by Django 3.2.5 on 2021-08-12 23:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0005_auto_20210813_0125'),
    ]

    operations = [
        migrations.RenameField(
            model_name='surveyresults',
            old_name='user',
            new_name='survey_user',
        ),
    ]