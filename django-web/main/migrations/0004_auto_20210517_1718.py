# Generated by Django 3.2.3 on 2021-05-17 08:18

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_post_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='mainImage',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(default=1, upload_to='uploaded_photo/%m/%d'),
            preserve_default=False,
        ),
    ]