# Generated by Django 3.2.5 on 2021-08-28 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='sender',
            field=models.CharField(default='BioBot', max_length=6),
        ),
    ]