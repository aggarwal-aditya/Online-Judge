# Generated by Django 4.0.5 on 2022-07-09 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0014_coderunner_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]
