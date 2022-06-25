from django.db import models
from django.template.defaultfilters import slugify
from mptt.models import MPTTModel, TreeForeignKey


# Create your models here.

class Category(MPTTModel):
	"""Категорії"""
	category_name = models.CharField(max_length=200, db_index=True, null=True, blank=True,
	                                 verbose_name='назва категорії')
	slug = models.SlugField(max_length=200, unique=True, null=True, blank=True, verbose_name='посилання')
	parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.PROTECT,
	                           verbose_name='батьківська категорія')
	category_image = models.ImageField(upload_to='media/category', blank=True, null=True,
	                                   verbose_name="Зображення категорії")
	description = models.TextField(blank=True, null=True, verbose_name='опис категорії')
	meta_title = models.CharField(max_length=200, blank=True, null=True, verbose_name='мета-заголовок')
	meta_keywords = models.CharField(max_length=200, blank=True, null=True, verbose_name='мета-теги')
	meta_description = models.CharField(max_length=200, blank=True, null=True, verbose_name='мета-опис')
	is_active = models.BooleanField(default=True, null=True, blank=True, verbose_name="Активна?")
	is_featured = models.BooleanField(default=False, null=True, blank=True, verbose_name="Відображена на головній?")

	class Meta:
		unique_together = ('slug', 'parent',)
		verbose_name = 'Категорія'
		verbose_name_plural = 'Категорії'
		ordering = ('-category_name',)

	def __str__(self):
		full_path = [self.category_name]
		k = self.parent
		while k is not None:
			full_path.append(k.category_name)
			k = k.parent

		return ' -> '.join(full_path[::-1])


class Product(models.Model):
	"""Товар"""
	category = models.ForeignKey(Category, related_name='products', null=True, blank=True, on_delete=models.PROTECT)
	product_name = models.CharField(max_length=200, db_index=True, null=True, blank=True, verbose_name='назва товару')
	slug = models.SlugField(max_length=200, unique=True, null=True, blank=True, verbose_name='посилання')
	image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, null=True, verbose_name='зображення')
	meta_title = models.CharField(max_length=200, blank=True, null=True, verbose_name='мета-заголовок')
	meta_keywords = models.CharField(max_length=200, blank=True, null=True, verbose_name='мета-теги')
	meta_description = models.CharField(max_length=200, blank=True, null=True, verbose_name='мета-опис')
	description = models.TextField(blank=True, null=True, verbose_name='опис')
	price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name='ціна')
	old_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name='стара ціна')
	is_active = models.BooleanField(default=True, null=True, blank=True, verbose_name="Активний?")
	is_featured = models.BooleanField(default=False, null=True, blank=True, verbose_name="Відображена на головній?")
	stock = models.PositiveIntegerField(verbose_name='кількість', default=0, blank=True, null=True)
	sku = models.CharField(max_length=200, blank=True, null=True, verbose_name='артикул')
	available = models.BooleanField(default=True, null=True, blank=True, verbose_name='Наявність')

	class Meta:
		ordering = ('-product_name',)
		verbose_name = 'товар'
		verbose_name_plural = 'товари'

	def __str__(self):
		return self.product_name

	@staticmethod
	def get_available_products():
		return Product.objects.filter(available=True).order_by('product_name', 'category_name', 'price', 'stock')

	def __str__(self):
		return f'{self.product_name} ({self.category.category_name}, {self.category.parent})'
