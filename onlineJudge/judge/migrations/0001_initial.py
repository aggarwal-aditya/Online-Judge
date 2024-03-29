# Generated by Django 4.0.5 on 2022-06-30 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problemId', models.IntegerField()),
                ('problemText', models.TextField()),
                ('difficulty', models.CharField(max_length=15)),
                ('status', models.CharField(max_length=15)),
                ('score', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.CharField(max_length=20)),
                ('totalScore', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TestCases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expectedInput', models.TextField()),
                ('expectedOutput', models.TextField()),
                ('problems', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='judge.problems')),
            ],
        ),
        migrations.CreateModel(
            name='Submissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('verdict', models.CharField(max_length=15)),
                ('problems', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='judge.problems')),
            ],
        ),
    ]
