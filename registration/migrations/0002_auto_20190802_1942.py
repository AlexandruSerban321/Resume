# Generated by Django 2.2.2 on 2019-08-02 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='biography',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='company',
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
