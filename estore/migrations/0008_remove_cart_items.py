# Generated by Django 2.1 on 2018-08-11 04:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estore', '0007_order_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='items',
        ),
    ]
