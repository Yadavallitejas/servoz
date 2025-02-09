# Generated by Django 5.1.4 on 2025-02-01 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(max_length=255)),
                ('cat_image', models.ImageField(upload_to='photos/categories')),
            ],
        ),
    ]
