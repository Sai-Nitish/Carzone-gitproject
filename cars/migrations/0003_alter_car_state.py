# Generated by Django 4.0.6 on 2022-08-05 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_alter_car_doors_alter_car_fuel_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='state',
            field=models.CharField(choices=[('AN', 'Andaman and Nicobar'), ('AP', 'Andhra Pradesh'), ('AR', 'Arunachal Pradesh'), ('AS', 'Assam'), ('BR', 'Bihar'), ('CH', 'Chandigarh'), ('DN', 'Dadra and Nagar Haveli'), ('DD', 'Daman and Diu'), ('DL', 'Delhi'), ('GA', 'Goa'), ('GJ', 'Gujarat'), ('HR', 'Haryana'), ('HP', 'Himacha Pradesh'), ('JK', 'Jammu and Kashmir'), ('KA', 'Karnataka'), ('KL', 'Kerala'), ('LD', 'Lakshadweep'), ('MP', 'Madhya Pradesh'), ('MH', 'Maharashtra'), ('MN', 'Manipur'), ('ML', 'Meghalaya'), ('MZ', 'Mizoram'), ('NL', 'Nagaland'), ('OR', 'Orissa'), ('PY', 'Pondicherry'), ('PN', 'Punjab'), ('RJ', 'Rajasthan'), ('SK', 'sikkim'), ('TN', 'Tamil Nadu'), ('TR', 'Tripura'), ('UP', 'Uttar Pradesh'), ('WB', 'West Bengal'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')], max_length=100),
        ),
    ]
