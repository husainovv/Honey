# Generated by Django 4.0.3 on 2022-03-12 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_products_image_alter_products_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.ImageField(default='default.png', upload_to=''),
        ),
    ]