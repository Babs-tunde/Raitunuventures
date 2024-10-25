# Generated by Django 4.2 on 2024-10-14 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_storebook_storebookentry_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='storebookentry',
            name='profit',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=15),
        ),
    ]