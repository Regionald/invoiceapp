# Generated by Django 4.0.2 on 2022-02-21 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='accountNumber',
            field=models.IntegerField(default=1541048928),
        ),
        migrations.AddField(
            model_name='user',
            name='companyAddress',
            field=models.CharField(default='No address', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='companyName',
            field=models.CharField(default='No name', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='logoName',
            field=models.CharField(default='logo', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='postalCode',
            field=models.IntegerField(default=1540),
        ),
        migrations.AddField(
            model_name='user',
            name='town',
            field=models.CharField(default='no town', max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]