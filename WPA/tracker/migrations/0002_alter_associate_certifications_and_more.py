# Generated by Django 5.1.3 on 2024-11-22 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tracker", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="associate",
            name="certifications",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="associates",
                to="tracker.certification",
            ),
        ),
        migrations.AlterField(
            model_name="associate",
            name="deducted_points",
            field=models.DecimalField(decimal_places=1, default=0, max_digits=3),
        ),
        migrations.AlterField(
            model_name="associate",
            name="points",
            field=models.DecimalField(decimal_places=1, default=0, max_digits=3),
        ),
        migrations.AlterField(
            model_name="project",
            name="associates",
            field=models.ManyToManyField(
                blank=True, null=True, related_name="projects", to="tracker.associate"
            ),
        ),
    ]
