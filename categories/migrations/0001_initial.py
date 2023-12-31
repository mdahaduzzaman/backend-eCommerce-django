# Generated by Django 4.2.7 on 2023-11-20 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainCategory',
            fields=[
                ('id', models.CharField(editable=False, max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='main_category_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.CharField(editable=False, max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='sub_category_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('main_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.maincategory')),
            ],
        ),
        migrations.CreateModel(
            name='SubSubCategory',
            fields=[
                ('id', models.CharField(editable=False, max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='sub_sub_category_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sub_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.subcategory')),
            ],
        ),
    ]
