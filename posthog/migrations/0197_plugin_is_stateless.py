# Generated by Django 3.2.5 on 2022-01-17 19:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posthog", "0196_update_property_types"),
    ]

    operations = [
        migrations.AddField(
            model_name="plugin",
            name="is_stateless",
            field=models.BooleanField(default=False, null=True, blank=True),
        ),
    ]
