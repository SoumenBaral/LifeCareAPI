# Generated by Django 4.2.7 on 2024-01-08 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='review',
            new_name='reviewer',
        ),
    ]
