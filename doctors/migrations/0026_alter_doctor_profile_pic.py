# Generated by Django 3.2.7 on 2021-11-12 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0025_auto_20211112_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='profile_pic',
            field=models.ImageField(blank=True, default='person.jpg', null=True, upload_to=''),
        ),
    ]
