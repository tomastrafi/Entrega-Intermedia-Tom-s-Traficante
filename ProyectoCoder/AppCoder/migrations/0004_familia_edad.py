# Generated by Django 4.1.3 on 2022-12-08 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0003_remove_familia_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='familia',
            name='edad',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
