# Generated by Django 4.1 on 2022-08-24 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("newsapp", "0003_alter_sentences_category_id_alter_sentences_url_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sentences",
            name="sentence_de",
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name="sentences",
            name="sentence_jp",
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name="words", name="word_de", field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name="words", name="word_jp", field=models.CharField(max_length=1000),
        ),
    ]
