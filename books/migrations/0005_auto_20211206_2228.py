# Generated by Django 3.2.7 on 2021-12-06 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_rename_edition_key_favouritebook_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favouritebook',
            name='author_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='favouritebook',
            name='key',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='favouritebook',
            name='title',
            field=models.CharField(max_length=200, unique=True, verbose_name='name'),
        ),
    ]
