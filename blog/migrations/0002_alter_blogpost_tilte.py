# Generated by Django 4.0.6 on 2022-08-29 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='tilte',
            field=models.TextField(),
        ),
    ]
