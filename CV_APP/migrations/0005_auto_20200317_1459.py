# Generated by Django 3.0.4 on 2020-03-17 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CV_APP', '0004_auto_20200316_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
