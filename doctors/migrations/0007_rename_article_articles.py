# Generated by Django 3.2.7 on 2021-11-04 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0006_rename_new_news'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='article',
            new_name='Articles',
        ),
    ]