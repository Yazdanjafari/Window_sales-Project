# Generated by Django 5.0.7 on 2024-07-13 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CV_App', '0002_alter_installed_installed_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='Profile_img',
            field=models.ImageField(upload_to='Comment'),
        ),
        migrations.AlterField(
            model_name='installed',
            name='Installed_Img',
            field=models.ImageField(help_text='لطفا سایز عکس یک در یک یا همان مربع باشد', upload_to='Installed_Img'),
        ),
    ]
