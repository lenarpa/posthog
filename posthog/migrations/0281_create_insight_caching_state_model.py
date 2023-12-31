# Generated by Django 3.2.15 on 2022-11-29 14:06

import django.db.models.deletion
from django.db import migrations, models

import posthog.models.utils


class Migration(migrations.Migration):
    dependencies = [
        ("posthog", "0280_fix_async_deletion_team"),
    ]

    operations = [
        migrations.CreateModel(
            name="InsightCachingState",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=posthog.models.utils.UUIDT,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("cache_key", models.CharField(max_length=400)),
                ("target_cache_age_seconds", models.IntegerField(null=True)),
                ("last_refresh", models.DateTimeField(blank=True, null=True)),
                ("last_refresh_queued_at", models.BooleanField(null=True)),
                ("refresh_attempt", models.IntegerField(default=0)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "dashboard_tile",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="caching_state",
                        to="posthog.dashboardtile",
                    ),
                ),
                (
                    "insight",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="caching_state",
                        to="posthog.insight",
                    ),
                ),
                (
                    "team",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="posthog.team"),
                ),
            ],
        ),
        migrations.AddIndex(
            model_name="insightcachingstate",
            index=models.Index(fields=["cache_key"], name="filter_by_cache_key_idx"),
        ),
        migrations.AddConstraint(
            model_name="insightcachingstate",
            constraint=models.UniqueConstraint(
                condition=models.Q(("insight__isnull", False)),
                fields=("insight",),
                name="unique_insight_for_caching_state_idx",
            ),
        ),
        migrations.AddConstraint(
            model_name="insightcachingstate",
            constraint=models.UniqueConstraint(
                condition=models.Q(("dashboard_tile__isnull", False)),
                fields=("insight", "dashboard_tile"),
                name="unique_dashboard_tile_idx",
            ),
        ),
    ]
