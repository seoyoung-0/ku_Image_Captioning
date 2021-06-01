# Generated by Django 3.2.3 on 2021-05-17 07:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='mainImage',
            field=models.ImageField(null=True, upload_to='uploaded_photo/%Y/%m/%d'),
        ),
    ]