# Generated by Django 2.2.3 on 2019-09-06 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20190906_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='image',
            field=models.ImageField(default='profile.png', upload_to='media/account/images'),
        ),
    ]
