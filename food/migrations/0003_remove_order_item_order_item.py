# Generated by Django 4.0.5 on 2022-06-24 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_alter_subcategory_name_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='item',
        ),
        migrations.AddField(
            model_name='order',
            name='item',
            field=models.ManyToManyField(related_name='order', to='food.food'),
        ),
    ]
