# Generated by Django 2.2.16 on 2021-01-29 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainhome', '0002_demo_book'),
    ]

    operations = [
        migrations.RenameField(
            model_name='demo_book',
            old_name='edtech',
            new_name='email',
        ),
    ]
