# Generated by Django 3.0.3 on 2020-04-27 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20200427_1637'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['publish_date']},
        ),
        migrations.AlterField(
            model_name='post',
            name='publish_date',
            field=models.DateField(auto_now=True),
        ),
    ]