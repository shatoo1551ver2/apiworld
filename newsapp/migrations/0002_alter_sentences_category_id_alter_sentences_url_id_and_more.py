# Generated by Django 4.1 on 2022-08-24 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("newsapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sentences", name="category_id", field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="sentences", name="url_id", field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="words", name="category_id", field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="words", name="url_id", field=models.IntegerField(),
        ),
    ]
