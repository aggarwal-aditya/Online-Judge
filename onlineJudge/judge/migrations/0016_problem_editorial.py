# Generated by Django 4.0.5 on 2022-07-09 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0015_alter_submission_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='editorial',
            field=models.URLField(blank=True, null=True),
        ),
    ]
