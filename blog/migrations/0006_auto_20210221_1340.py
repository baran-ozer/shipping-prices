# Generated by Django 3.1.6 on 2021-02-21 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210221_1324'),
    ]

    operations = [
        migrations.RenameField(
            model_name='yazilarmodel',
            old_name='duzellenme_tarihi',
            new_name='duzenlenme_tarihi',
        ),
    ]
