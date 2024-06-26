# Generated by Django 5.0.6 on 2024-06-16 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0005_alter_booking_check_in_alter_booking_check_out'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='total_price',
            field=models.PositiveBigIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='room',
            name='price',
            field=models.PositiveIntegerField(),
        ),
    ]
