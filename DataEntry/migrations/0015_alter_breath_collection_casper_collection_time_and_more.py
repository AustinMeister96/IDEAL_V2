# Generated by Django 4.2.3 on 2023-11-06 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("DataEntry", "0014_alter_breath_collection_collection_start_time_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="breath_collection",
            name="casper_collection_time",
            field=models.TimeField(
                blank=True, null=True, verbose_name="casper collection time"
            ),
        ),
        migrations.AlterField(
            model_name="breath_collection",
            name="tennax_number",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
