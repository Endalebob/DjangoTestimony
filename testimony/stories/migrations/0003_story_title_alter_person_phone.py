# Generated by Django 4.0.2 on 2022-03-03 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0002_alter_person_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='title',
            field=models.CharField(help_text='Title of story', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone',
            field=models.CharField(help_text='phone number', max_length=15),
        ),
    ]