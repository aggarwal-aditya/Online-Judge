# Generated by Django 4.0.5 on 2022-07-09 13:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0013_rename_executable_coderunner'),
    ]

    operations = [
        migrations.AddField(
            model_name='coderunner',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 9, 13, 17, 10, 419028, tzinfo=utc), verbose_name='date published'),
            preserve_default=False,
        ),
    ]
