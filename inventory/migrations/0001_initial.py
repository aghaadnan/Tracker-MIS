# Generated by Django 3.1.4 on 2023-03-02 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msisdn', models.CharField(max_length=255)),
                ('icc_id', models.CharField(max_length=255)),
                ('operator', models.CharField(max_length=255)),
                ('package', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TrackerDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_number', models.CharField(max_length=255)),
                ('vendor', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('imei', models.CharField(max_length=255)),
            ],
        ),
    ]
