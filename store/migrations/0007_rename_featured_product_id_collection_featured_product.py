# Generated by Django 3.2.5 on 2021-08-02 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_remove_collection_discount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collection',
            old_name='featured_product_id',
            new_name='featured_product',
        ),
    ]
