# Generated by Django 3.0.3 on 2020-04-27 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200427_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
