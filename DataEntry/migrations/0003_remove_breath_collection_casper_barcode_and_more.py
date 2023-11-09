# Generated by Django 4.2.3 on 2023-10-24 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("DataEntry", "0002_alter_breath_collection_collection_time"),
    ]

    operations = [
        migrations.RemoveField(model_name="breath_collection", name="casper_barcode",),
        migrations.RemoveField(model_name="breath_collection", name="reciva_barcode",),
        migrations.RemoveField(
            model_name="breath_collection", name="room_air_barcode",
        ),
        migrations.AlterField(
            model_name="breath_collection",
            name="casper_tennax",
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name="breath_collection",
            name="room_air_tennax",
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name="breath_collection",
            name="tennax_number",
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]