# Generated by Django 4.2.7 on 2023-11-30 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_item_discount_item_off'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='final_price',
            field=models.DecimalField(decimal_places=2, default=1, editable=False, max_digits=10),
            preserve_default=False,
        ),
    ]