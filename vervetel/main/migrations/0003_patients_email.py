# Generated by Django 4.2.2 on 2023-06-13 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_datetimes'),
    ]

    operations = [
        migrations.AddField(
            model_name='patients',
            name='email',
            field=models.EmailField(default='xy@gmail.com', max_length=254),
        ),
    ]
