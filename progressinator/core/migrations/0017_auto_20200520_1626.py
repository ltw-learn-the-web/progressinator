# Generated by Django 3.0.6 on 2020-05-20 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("progress_core", "0016_auto_20190411_0135"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="course",
            options={
                "ordering": ("term", "order"),
                "verbose_name": "course",
                "verbose_name_plural": "courses",
            },
        ),
        migrations.AlterModelOptions(
            name="userprofile",
            options={
                "get_latest_by": "created",
                "ordering": ("-id", "user"),
                "verbose_name": "user profile",
                "verbose_name_plural": "user profile",
            },
        ),
    ]