# Generated by Django 4.2.7 on 2023-12-29 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_alter_item_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='published_date',
            field=models.DateTimeField(),
        ),
    ]
