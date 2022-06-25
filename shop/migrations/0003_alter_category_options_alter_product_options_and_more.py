# Generated by Django 4.0.5 on 2022-06-10 23:15

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_childcategory_category_alter_product_category_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('-created_at',), 'verbose_name': 'Категорія', 'verbose_name_plural': 'Категорії'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-created_at',), 'verbose_name': 'товар', 'verbose_name_plural': 'товари'},
        ),
        migrations.RemoveField(
            model_name='product',
            name='child_category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='created',
        ),
        migrations.RemoveField(
            model_name='product',
            name='updated',
        ),
        migrations.AddField(
            model_name='category',
            name='category_image',
            field=models.ImageField(blank=True, null=True, upload_to='media/category', verbose_name='Зображення категорії'),
        ),
        migrations.AddField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата створення'),
        ),
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='опис категорії'),
        ),
        migrations.AddField(
            model_name='category',
            name='is_active',
            field=models.BooleanField(blank=True, default=True, null=True, verbose_name='Активна?'),
        ),
        migrations.AddField(
            model_name='category',
            name='is_featured',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Відображена на головній?'),
        ),
        migrations.AddField(
            model_name='category',
            name='level',
            field=models.PositiveIntegerField(default=0, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='lft',
            field=models.PositiveIntegerField(default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='meta_description',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='мета-опис'),
        ),
        migrations.AddField(
            model_name='category',
            name='meta_keywords',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='мета-теги'),
        ),
        migrations.AddField(
            model_name='category',
            name='meta_title',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='мета-заголовок'),
        ),
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='shop.category', verbose_name='батьківська категорія'),
        ),
        migrations.AddField(
            model_name='category',
            name='rght',
            field=models.PositiveIntegerField(default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='tree_id',
            field=models.PositiveIntegerField(db_index=True, default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Дата оновлення'),
        ),
        migrations.AddField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата створення'),
        ),
        migrations.AddField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(blank=True, default=True, null=True, verbose_name='Активний?'),
        ),
        migrations.AddField(
            model_name='product',
            name='is_featured',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Відображена на головній?'),
        ),
        migrations.AddField(
            model_name='product',
            name='meta_description',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='мета-опис'),
        ),
        migrations.AddField(
            model_name='product',
            name='meta_keywords',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='мета-теги'),
        ),
        migrations.AddField(
            model_name='product',
            name='meta_title',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='мета-заголовок'),
        ),
        migrations.AddField(
            model_name='product',
            name='old_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='стара ціна'),
        ),
        migrations.AddField(
            model_name='product',
            name='sku',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='артикул'),
        ),
        migrations.AddField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Дата оновлення'),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(blank=True, db_index=True, max_length=200, null=True, verbose_name='назва категорії'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='посилання'),
        ),
        migrations.AlterField(
            model_name='product',
            name='available',
            field=models.BooleanField(blank=True, default=True, null=True, verbose_name='Наявність'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='products', to='shop.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='опис'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products/%Y/%m/%d', verbose_name='зображення'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='ціна'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(blank=True, db_index=True, max_length=200, null=True, verbose_name='назва товару'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='посилання'),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='кількість'),
        ),
        migrations.AlterUniqueTogether(
            name='category',
            unique_together={('slug', 'parent')},
        ),
        migrations.DeleteModel(
            name='ChildCategory',
        ),
    ]
