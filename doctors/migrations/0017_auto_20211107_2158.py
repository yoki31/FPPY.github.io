# Generated by Django 3.2.6 on 2021-11-07 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0016_auto_20211107_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='img',
            field=models.ImageField(default='defbg.png', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='new',
            name='img',
            field=models.ImageField(default='defbg.png', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='package',
            name='img',
            field=models.ImageField(default='defbg.png', null=True, upload_to=''),
        ),
    ]