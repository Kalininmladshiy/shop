# Generated by Django 4.1.5 on 2023-02-21 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_order_orderitem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='firstname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='lastname',
            new_name='last_name',
        ),
    ]