# Generated by Django 3.2.6 on 2021-11-11 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0023_auto_20211111_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buy',
            name='package',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='doctors.package'),
        ),
        migrations.AlterField(
            model_name='buy',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='doctors.patient'),
        ),
    ]
