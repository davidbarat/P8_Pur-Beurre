# Generated by Django 3.1.1 on 2020-09-23 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.CharField(max_length=200)),
                ('picture_path', models.URLField()),
                ('nutriscore_grade', models.CharField(max_length=1)),
                ('categories', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='search.categories')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email_address', models.EmailField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Substitute',
            fields=[
                ('products_barcode', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='search.products')),
                ('products_selected', models.CharField(max_length=20)),
            ],
        ),
    ]