# Generated by Django 4.0.5 on 2022-07-04 19:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0003_review"),
    ]

    operations = [
        migrations.AddField(
            model_name="review",
            name="rating",
            field=models.IntegerField(
                default=3,
                validators=[
                    django.core.validators.MaxValueValidator(5),
                    django.core.validators.MinValueValidator(1),
                ],
            ),
        ),
    ]
