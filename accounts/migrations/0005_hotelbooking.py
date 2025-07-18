# Generated by Django 5.1.4 on 2025-05-19 05:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_amenities_alter_hotel_hotel_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotelBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_start_date', models.DateField()),
                ('booking_end_date', models.DateField()),
                ('price', models.FloatField()),
                ('booking_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.hoteluser')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='accounts.hotel')),
            ],
        ),
    ]
