# Generated by Django 4.2.2 on 2023-07-08 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_rewiew_stars'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.ManyToManyField(blank=True, null=True, to='product.product')),
            ],
        ),
    ]
