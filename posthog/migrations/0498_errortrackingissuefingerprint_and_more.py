# Generated by Django 4.2.15 on 2024-10-24 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("posthog", "0497_experimentholdout_experiment_holdout"),
    ]

    operations = [
        migrations.CreateModel(
            name="ErrorTrackingIssueFingerprint",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("fingerprint", models.TextField()),
                ("version", models.BigIntegerField(blank=True, default=0)),
                (
                    "issue",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="posthog.errortrackinggroup"),
                ),
                (
                    "team",
                    models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, to="posthog.team"),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="errortrackingissuefingerprint",
            constraint=models.UniqueConstraint(fields=("team", "fingerprint"), name="unique fingerprint for team"),
        ),
    ]