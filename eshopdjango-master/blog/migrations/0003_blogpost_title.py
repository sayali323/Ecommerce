# Generated by Django 2.2.14 on 2020-12-11 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201211_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='title',
            field=models.CharField(default='null', max_length=50),
        ),
    ]
