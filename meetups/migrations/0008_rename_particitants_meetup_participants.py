# Generated by Django 3.2.4 on 2021-06-26 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0007_alter_meetup_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meetup',
            old_name='particitants',
            new_name='participants',
        ),
    ]