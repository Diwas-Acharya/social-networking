# Generated by Django 2.2.3 on 2019-09-06 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_details_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='image',
            field=models.ImageField(default='profile.png', upload_to='account/images'),
        ),
    ]
