# Generated by Django 4.0.5 on 2022-06-08 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='childcategory',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='child_category', to='shop.category', verbose_name='категорія'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='shop.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='child_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='shop.childcategory'),
        ),
    ]
