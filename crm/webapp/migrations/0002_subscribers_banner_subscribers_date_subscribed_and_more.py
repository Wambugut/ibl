# Generated by Django 5.0.6 on 2024-05-21 17:13

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscribers',
            name='banner',
            field=models.ImageField(blank='true', default='fallback.png', upload_to=''),
        ),
        migrations.AddField(
            model_name='subscribers',
            name='date_subscribed',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='subscribers',
            name='email',
            field=models.EmailField(default=1, max_length=254, unique=True),
            preserve_default=False,
        ),
    ]
