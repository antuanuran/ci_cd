# Generated by Django 4.2.5 on 2023-11-14 06:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("products", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="vendor",
            name="owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="vendors", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="products", to="products.category"
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="vendor",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="products", to="products.vendor"
            ),
        ),
        migrations.AddField(
            model_name="itemparameter",
            name="attribute",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="parameters", to="products.attribute"
            ),
        ),
        migrations.AddField(
            model_name="itemparameter",
            name="item",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="parameters", to="products.item"
            ),
        ),
        migrations.AddField(
            model_name="item",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="items", to="products.product"
            ),
        ),
        migrations.AddField(
            model_name="attribute",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="attributes", to="products.product"
            ),
        ),
    ]
