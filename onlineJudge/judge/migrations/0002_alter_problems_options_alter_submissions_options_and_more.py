# Generated by Django 4.0.5 on 2022-06-30 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='problems',
            options={'verbose_name_plural': 'PluralForMyModel'},
        ),
        migrations.AlterModelOptions(
            name='submissions',
            options={'verbose_name_plural': 'PluralForMyModel'},
        ),
        migrations.AlterModelOptions(
            name='testcases',
            options={'verbose_name_plural': 'PluralForMyModel'},
        ),
    ]
