from django.db import models

# Create your models here.

class Post(models.Model):
    category = models.ForeignKey("Category", on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=150, verbose_name="Title")
    text = models.TextField(max_length=250, verbose_name="Text")
    price = models.DecimalField(max_digits=7, decimal_places=2)
    created_date = models.DateTimeField(verbose_name="Created date", auto_now_add=True)
    published_date = models.DateTimeField(verbose_name="published date", auto_now=False)

    def __str__(self) -> str:
        return f"{self.title}"


class Category(models.Model):
    title = models.CharField(verbose_name="title", max_length=150)

    def __str__(self) -> str:
        return f"{self.title}"

class Basket(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    product = models.ManyToManyField('Post', related_name='product_basket')

    def __str__(self):
        return f'{self.user}'

