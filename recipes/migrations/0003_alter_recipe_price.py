# Generated by Django 3.2.7 on 2022-09-21 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20220921_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='price',
            field=models.FloatField(blank=True, null=True, verbose_name='Цена'),
        ),
    ]