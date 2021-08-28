# Generated by Django 3.2.5 on 2021-08-28 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('username', models.CharField(default='You', max_length=120)),
            ],
            options={
                'ordering': ('date',),
            },
        ),
    ]
