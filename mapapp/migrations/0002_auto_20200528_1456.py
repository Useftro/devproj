# Generated by Django 3.0.6 on 2020-05-28 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='point',
            old_name='latitude',
            new_name='lat',
        ),
        migrations.RenameField(
            model_name='point',
            old_name='longitude',
            new_name='lng',
        ),
    ]