# Generated by Django 3.1.6 on 2021-02-17 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productdetail', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]