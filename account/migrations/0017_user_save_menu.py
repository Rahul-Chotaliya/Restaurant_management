# Generated by Django 4.2.4 on 2023-08-25 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0016_remove_user_resturant_name_remove_user_save_menu_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='save_menu',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
