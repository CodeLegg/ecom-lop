# Generated by Django 5.0.3 on 2024-04-19 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_color_remove_product_color_product_colors'),
    ]

    operations = [
        migrations.AddField(
            model_name='color',
            name='hex_code',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
    ]
