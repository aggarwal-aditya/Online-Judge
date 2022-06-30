# Generated by Django 4.0.5 on 2022-06-30 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0002_alter_problems_options_alter_submissions_options_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Problems',
            new_name='Problem',
        ),
        migrations.RenameModel(
            old_name='Submissions',
            new_name='Submission',
        ),
        migrations.RenameModel(
            old_name='TestCases',
            new_name='TestCase',
        ),
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
        migrations.AlterModelOptions(
            name='problem',
            options={},
        ),
        migrations.AlterModelOptions(
            name='submission',
            options={},
        ),
        migrations.AlterModelOptions(
            name='testcase',
            options={},
        ),
    ]
