# Generated by Django 3.2.6 on 2021-11-07 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0014_auto_20211107_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='img',
            field=models.ImageField(null=True, upload_to='images/packages'),
        ),
    ]
