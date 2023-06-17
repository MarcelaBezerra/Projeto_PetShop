# Generated by Django 4.2.2 on 2023-06-13 01:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agendamentos', '0001_initial'),
        ('servicos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adestramento',
            name='age_codigo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='agendamentos.agendamentos'),
        ),
        migrations.AlterField(
            model_name='banhoetosa',
            name='age_codigo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='agendamentos.agendamentos'),
        ),
        migrations.AlterField(
            model_name='consultas',
            name='age_codigo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='agendamentos.agendamentos'),
        ),
    ]