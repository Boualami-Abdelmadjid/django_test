# Generated by Django 5.0 on 2023-12-15 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receipt',
            old_name='purchase_data',
            new_name='purchase_date',
        ),
    ]
