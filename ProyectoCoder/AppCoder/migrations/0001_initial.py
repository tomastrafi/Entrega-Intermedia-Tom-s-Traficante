# Generated by Django 4.1.3 on 2022-11-23 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('rol', models.CharField(max_length=40)),
                ('trabajo', models.CharField(max_length=40)),
                ('edad', models.IntegerField()),
                ('fecha', models.DateField()),
            ],
        ),
    ]
