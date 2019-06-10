# Generated by Django 2.1.4 on 2019-05-31 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('payment', '0003_remove_payment_contract'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='contract',
            field=models.ForeignKey(default=1, on_delete='cascade', to='core.Contract'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payment',
            name='payment_value',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
