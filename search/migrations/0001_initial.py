# Generated by Django 3.1.1 on 2020-11-02 17:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("category_name", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                ("product_id", models.AutoField(primary_key=True, serialize=False)),
                ("barcode", models.BigIntegerField()),
                ("product_name", models.CharField(default="na", max_length=100)),
                ("resume", models.CharField(max_length=1000)),
                ("picture_path", models.URLField()),
                ("small_picture_path", models.URLField()),
                ("nutriscore_grade", models.CharField(max_length=2)),
                ("url", models.URLField()),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="search.category",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DetailProduct",
            fields=[
                (
                    "id",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="search.product",
                    ),
                ),
                ("energy_100g", models.DecimalField(decimal_places=2, max_digits=7)),
                ("energy_unit", models.CharField(max_length=5)),
                ("proteins_100g", models.DecimalField(decimal_places=2, max_digits=6)),
                ("fat_100g", models.DecimalField(decimal_places=2, max_digits=6)),
                (
                    "saturated_fat_100g",
                    models.DecimalField(decimal_places=2, max_digits=6),
                ),
                (
                    "carbohydrates_100g",
                    models.DecimalField(decimal_places=2, max_digits=6),
                ),
                ("sugars_100g", models.DecimalField(decimal_places=2, max_digits=6)),
                ("fiber_100g", models.DecimalField(decimal_places=2, max_digits=6)),
                ("salt_100g", models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name="Substitute",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "substitute_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="search.product"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
