# Generated by Django 4.2.2 on 2023-06-10 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_alter_login_log_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='log_codigo',
            field=models.IntegerField(editable=False, primary_key=True, serialize=False),
        ),
    ]