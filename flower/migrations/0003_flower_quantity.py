# Generated by Django 4.2.7 on 2024-01-31 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flower', '0002_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='flower',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]