# Generated by Django 3.0.8 on 2020-08-14 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='catagory',
            field=models.CharField(default='all_item', max_length=20),
        ),
    ]
