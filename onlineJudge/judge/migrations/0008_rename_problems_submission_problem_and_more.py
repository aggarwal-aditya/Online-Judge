# Generated by Django 4.0.5 on 2022-07-05 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0007_rename_problem_submission_problems_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submission',
            old_name='problems',
            new_name='problem',
        ),
        migrations.RenameField(
            model_name='testcase',
            old_name='problems',
            new_name='problem',
        ),
    ]
