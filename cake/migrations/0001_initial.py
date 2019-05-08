# Generated by Django 2.2.1 on 2019-05-08 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cake',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('modified_timestamp', models.DateTimeField(auto_now=True)),
                ('display_name', models.CharField(blank=True, max_length=255, null=True)),
                ('toppings_string', models.CharField(max_length=200)),
                ('max_slices', models.IntegerField()),
            ],
            options={
                'managed': True,
            },
        ),
    ]
