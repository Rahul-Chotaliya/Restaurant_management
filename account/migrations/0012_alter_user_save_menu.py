# Generated by Django 4.2.4 on 2023-08-25 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_remove_resturants_save_menu_user_resturant_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='save_menu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.menu', unique=True),
        ),
    ]
