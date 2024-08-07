# Generated by Django 5.0.7 on 2024-07-13 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(max_length=255)),
                ('user_name', models.CharField(max_length=255)),
                ('profile_photo', models.ImageField(upload_to='')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
