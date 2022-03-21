# Generated by Django 4.0.2 on 2022-03-03 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0002_user_accountnumber_user_companyaddress_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=30)),
                ('clientName', models.CharField(default='No name', max_length=60)),
                ('clientAddress', models.CharField(default='No name', max_length=60)),
                ('clientTown', models.CharField(default='No name', max_length=100)),
                ('clientpostalCode', models.IntegerField(default=1540)),
                ('descript', models.JSONField(default=[])),
                ('rate', models.JSONField(default=[])),
                ('qty', models.JSONField(default=[])),
                ('subTotal', models.IntegerField(default=0)),
                ('vat', models.IntegerField(default=0)),
                ('Total', models.IntegerField(default=0)),
            ],
        ),
    ]
