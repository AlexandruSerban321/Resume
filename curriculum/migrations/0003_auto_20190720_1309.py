# Generated by Django 2.2.2 on 2019-07-20 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0002_strenght'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.DeleteModel(
            name='Strenght',
        ),
    ]
