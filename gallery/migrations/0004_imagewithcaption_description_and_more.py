# Generated by Django 5.1.7 on 2025-04-23 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_imagewithcaption_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagewithcaption',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='imagewithcaption',
            name='dimensions',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='imagewithcaption',
            name='materials',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='imagewithcaption',
            name='rating',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
