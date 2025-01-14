# Generated by Django 3.2.6 on 2021-11-11 06:04

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0022_alter_appointment_doctor_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='dateapp',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='buy',
            name='status',
            field=models.CharField(choices=[('NOT PAID', 'NOT PAID'), ('PAID', 'PAID')], default='NOT PAID', max_length=200, null=True),
        ),
        migrations.CreateModel(
            name='Specialitie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spec', models.CharField(max_length=100, null=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='doctors.doctor')),
            ],
        ),
    ]
