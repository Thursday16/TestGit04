# Generated by Django 4.2.5 on 2023-10-02 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_app', '0003_player'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='email',
            field=models.CharField(max_length=20),
        ),
    ]
