# Generated by Django 3.0.4 on 2020-04-08 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='unique_id',
            field=models.CharField(editable=False, max_length=50, unique=True, verbose_name='unique id'),
        ),
    ]