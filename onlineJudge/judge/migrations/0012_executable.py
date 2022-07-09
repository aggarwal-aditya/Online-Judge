# Generated by Django 4.0.5 on 2022-07-09 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0011_programminglanguage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Executable',
            fields=[
                ('status', models.CharField(max_length=100)),
                ('userCode', models.TextField()),
                ('userLanguage', models.IntegerField()),
                ('queueNo', models.AutoField(primary_key=True, serialize=False)),
                ('testCase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='judge.testcase')),
            ],
        ),
    ]
