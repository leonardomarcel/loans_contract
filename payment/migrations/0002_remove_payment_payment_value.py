# Generated by Django 2.1.4 on 2019-05-31 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='payment_value',
        ),
    ]
