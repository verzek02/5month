from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, null=True)

    @property
    def product_count(self):
        return self.product_set.all().count()

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    @property
    def rating(self):
        total_amount = self.rewiew_set.all().count()
        if total_amount == 0:
            return 0
        sum_ = 0
        for i in self.rewiew_set.all():
            sum_ += i.stars
        return sum_ / total_amount


class Rewiew(models.Model):
    text = models.CharField(max_length=100, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    stars = models.PositiveIntegerField(default=1, verbose_name='Звезды', null=True)
