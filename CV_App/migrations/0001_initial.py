# Generated by Django 5.0.2 on 2024-07-13 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Profile_img', models.ImageField(upload_to='Personal')),
                ('Full_Name', models.CharField(max_length=55)),
                ('Phone_Number', models.CharField(max_length=11)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Installed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55)),
                ('Installed_Img', models.ImageField(upload_to='Personal')),
            ],
        ),
    ]