# Generated by Django 5.0.7 on 2024-07-13 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CV_App', '0003_alter_comment_profile_img_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='Profile_img',
            field=models.ImageField(blank=True, null=True, upload_to='Comment'),
        ),
    ]
