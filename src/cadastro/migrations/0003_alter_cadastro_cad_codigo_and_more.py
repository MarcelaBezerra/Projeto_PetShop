# Generated by Django 4.2.2 on 2023-06-10 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0002_alter_cadastro_cad_codigo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastro',
            name='cad_codigo',
            field=models.IntegerField(editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='logincadastro',
            name='lc_codigo',
            field=models.IntegerField(editable=False, primary_key=True, serialize=False),
        ),
    ]
