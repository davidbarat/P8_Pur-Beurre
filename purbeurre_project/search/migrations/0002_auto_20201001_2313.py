# Generated by Django 3.1.1 on 2020-10-01 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categories',
            new_name='Category',
        ),
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='categories',
            new_name='category',
        ),
    ]
