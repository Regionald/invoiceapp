# Generated by Django 4.0.2 on 2022-03-03 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0007_remove_clients_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clients',
            name='descript',
        ),
        migrations.RemoveField(
            model_name='clients',
            name='qty',
        ),
        migrations.RemoveField(
            model_name='clients',
            name='rate',
        ),
    ]
