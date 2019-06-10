# Generated by Django 2.2.1 on 2019-06-02 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('payment', '0005_remove_payment_contract'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='contract',
            field=models.ForeignKey(default=1, on_delete='cascade', to='core.Contract'),
            preserve_default=False,
        ),
    ]
