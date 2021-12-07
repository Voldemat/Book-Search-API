# Generated by Django 3.2.9 on 2021-12-05 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favouritebook',
            old_name='name',
            new_name='title',
        ),
        migrations.AddField(
            model_name='favouritebook',
            name='author_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='favouritebook',
            name='image',
            field=models.CharField(max_length=200, null=True),
        ),
    ]