# Generated by Django 3.1.4 on 2021-01-04 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210105_0314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='condition',
            field=models.CharField(choices=[('New', 'New'), ('Used', 'Used')], max_length=10),
        ),
    ]
