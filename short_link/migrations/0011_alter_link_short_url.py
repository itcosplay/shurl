# Generated by Django 4.0.2 on 2022-03-05 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('short_link', '0010_alter_link_short_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='short_url',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]