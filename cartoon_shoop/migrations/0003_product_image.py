# Generated by Django 2.2.12 on 2021-02-04 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartoon_shoop', '0002_orderitem_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]