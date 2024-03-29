# Generated by Django 4.0.5 on 2022-07-09 12:47

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('judge', '0009_alter_submission_verdict'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pointsEarned', models.FloatField(default=0)),
                ('solved', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None), size=None)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.RemoveField(
            model_name='problem',
            name='id',
        ),
        migrations.AddField(
            model_name='submission',
            name='cpuTime',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='submission',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='submission',
            name='userCode',
            field=models.TextField(default='Code for this submission is not available'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='problem',
            name='problemId',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
