# Generated by Django 2.2.1 on 2019-05-08 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cake', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cake',
            old_name='toppings_string',
            new_name='candies',
        ),
    ]