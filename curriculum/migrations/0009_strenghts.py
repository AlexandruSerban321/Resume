# Generated by Django 2.2.2 on 2019-11-08 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0008_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Strenghts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strenght', models.CharField(max_length=100)),
            ],
        ),
    ]