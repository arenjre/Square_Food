# Generated by Django 4.0.5 on 2022-06-28 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_listedrestaurants'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='Is_varified',
            field=models.BooleanField(default=False),
        ),
    ]