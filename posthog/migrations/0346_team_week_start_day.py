# Generated by Django 3.2.18 on 2023-06-23 15:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posthog", "0345_view_link_and_s3_table_update"),
    ]

    operations = [
        migrations.AddField(
            model_name="team",
            name="week_start_day",
            field=models.SmallIntegerField(blank=True, choices=[(0, "Sunday"), (1, "Monday")], null=True),
        ),
    ]
