# Generated by Django 4.2.7 on 2023-11-16 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_padaria', '0002_alter_reserva_data_reserva'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedido',
            old_name='data_pedido',
            new_name='data_hora_pedido',
        ),
        migrations.AlterField(
            model_name='reserva',
            name='quantidade_pessoas',
            field=models.IntegerField(),
        ),
    ]
