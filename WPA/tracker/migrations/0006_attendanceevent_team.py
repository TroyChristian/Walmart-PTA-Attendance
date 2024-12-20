# Generated by Django 5.1.2 on 2024-11-29 22:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tracker", "0005_associate_shift_time"),
    ]

    operations = [
        migrations.AddField(
            model_name="attendanceevent",
            name="team",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="team_attendance_events",
                to="tracker.team",
            ),
        ),
    ]
