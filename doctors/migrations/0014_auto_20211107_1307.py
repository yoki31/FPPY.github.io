# Generated by Django 3.2.7 on 2021-11-07 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0013_auto_20211105_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='img',
            field=models.ImageField(null=True, upload_to='images/articles'),
        ),
        migrations.AddField(
            model_name='new',
            name='img',
            field=models.ImageField(null=True, upload_to='images/news'),
        ),
    ]