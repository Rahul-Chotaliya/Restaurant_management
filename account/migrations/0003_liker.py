# Generated by Django 4.2.4 on 2023-08-24 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_delete_liker'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikeR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('resturant', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='account.resturants')),
            ],
        ),
    ]
