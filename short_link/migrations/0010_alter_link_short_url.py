# Generated by Django 4.0.2 on 2022-03-05 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('short_link', '0009_alter_link_coustom_url_alter_link_short_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='short_url',
            field=models.CharField(max_length=100),
        ),
    ]
