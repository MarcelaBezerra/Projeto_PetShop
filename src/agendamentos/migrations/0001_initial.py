# Generated by Django 4.2.2 on 2023-06-11 23:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0003_alter_login_log_codigo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agendamentos',
            fields=[
                ('age_codigo', models.IntegerField(editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='LoginAgendamento',
            fields=[
                ('la_codigo', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('age_codigo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='agendamentos.agendamentos')),
                ('log_codigo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='login.login')),
            ],
        ),
    ]
