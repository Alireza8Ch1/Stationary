# Generated by Django 4.2.7 on 2023-12-29 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_rename_emal_customer_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='published_date',
            field=models.DateTimeField(null=True,blank=True),
            preserve_default=False,
        ),
    ]
