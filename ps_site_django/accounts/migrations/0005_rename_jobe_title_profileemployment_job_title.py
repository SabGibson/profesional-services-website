# Generated by Django 4.2.1 on 2023-05-13 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0004_profile_thumbnail"),
    ]

    operations = [
        migrations.RenameField(
            model_name="profileemployment", old_name="jobe_title", new_name="job_title",
        ),
    ]