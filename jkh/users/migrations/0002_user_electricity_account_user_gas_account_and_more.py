# Generated by Django 5.0.6 on 2024-05-18 09:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="electricity_account",
            field=models.CharField(
                blank=True,
                max_length=12,
                unique=True,
                verbose_name="Лицевой счет по электроснабжению",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="gas_account",
            field=models.CharField(
                blank=True,
                max_length=12,
                unique=True,
                verbose_name="Лицевой счет по газоснабжению",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="water_account",
            field=models.CharField(
                blank=True,
                max_length=12,
                unique=True,
                verbose_name="Лицевой счет по водоснабжению",
            ),
        ),
    ]
