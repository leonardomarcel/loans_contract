# Generated by Django 2.1.4 on 2019-05-31 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateTimeField()),
                ('payment_value', models.IntegerField()),
                ('contract', models.ForeignKey(on_delete='cascade', to='core.Contract')),
            ],
        ),
    ]
