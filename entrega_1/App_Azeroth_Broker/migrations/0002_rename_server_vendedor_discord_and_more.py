# Generated by Django 4.0.4 on 2022-05-31 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_Azeroth_Broker', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendedor',
            old_name='Server',
            new_name='discord',
        ),
        migrations.RenameField(
            model_name='vendedor',
            old_name='apellido',
            new_name='juego',
        ),
        migrations.RemoveField(
            model_name='vendedor',
            name='email',
        ),
        migrations.RemoveField(
            model_name='vendedor',
            name='precio',
        ),
        migrations.RemoveField(
            model_name='vendedor',
            name='stock',
        ),
    ]
