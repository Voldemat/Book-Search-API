# Generated by Django 3.2.9 on 2021-12-05 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_favouritebook_edition_key'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favouritebook',
            old_name='edition_key',
            new_name='key',
        ),
    ]
