# Generated by Django 4.2.4 on 2023-08-25 05:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_alter_resturants_resturant_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='save_manu',
            new_name='save_menu',
        ),
    ]
