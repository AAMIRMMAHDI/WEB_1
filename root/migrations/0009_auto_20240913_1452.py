# Generated by Django 3.2.25 on 2024-09-13 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0008_auto_20240913_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='name10',
            field=models.CharField(default='test', max_length=100),
        ),
        migrations.AddField(
            model_name='about',
            name='name11',
            field=models.CharField(default='test', max_length=100),
        ),
    ]
