# Generated by Django 2.0.6 on 2018-06-12 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20180610_1234'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ManyToManyField(help_text="Enter book's natural language", to='catalog.Language'),
        ),
    ]
