# Generated by Django 4.2.2 on 2023-06-10 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='log_codigo',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
