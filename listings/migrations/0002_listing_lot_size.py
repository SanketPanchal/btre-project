# Generated by Django 2.1.4 on 2018-12-06 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='lot_size',
            field=models.DecimalField(decimal_places=1, default=1, max_digits=5),
        ),
    ]
