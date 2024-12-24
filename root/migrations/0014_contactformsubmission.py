# Generated by Django 4.2 on 2024-09-23 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0013_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactFormSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('response', models.TextField(blank=True, null=True)),
                ('is_approved', models.BooleanField(default=False)),
            ],
        ),
    ]
