from django.db import models


# Create your models here.
class Product(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    priceId = models.CharField(max_length=100)
    mainImage = models.CharField(max_length=200, default='image_url')
    subImage1 = models.CharField(max_length=200, default='image_url')
    subImage2 = models.CharField(max_length=200, default='image_url')
    REGIONS = (
      ("UK", "THE UNITED KINGDOM"),
      ("EU", "EUROPE"),
      ("USA", "USA"),
      ("AUS", "AUS"),
      ("ASIA", "ASIA"),
    )
    region = models.CharField(max_length=5, choices=REGIONS, default='UK')
    CURRENCIES = (
      ("USD", "US Dollar"),
      ("EURO", "Euro"),
      ("GBP", "Great Britain Pound"),
      ("BAT", "Basic Attention Token")
    )
    currency = models.CharField(max_length=5, choices=CURRENCIES, default='UK')
    STYLES = (
      ("Sweet", "Sweet"),
      ("Bitter", "Bitter"),
      ("Sour", "Sour"),
      ("Moon", "Moon"),
    )
    style = models.CharField(max_length=10, choices=STYLES, default='Sweet')
    THEMES = (
      ("One to watch", "One to watch"),
      ("Summer hits", "Summer hits"),
      ("Yorkshire", "Yorkshire"),
      ("Belgium", "Belgium"),
    )
    theme = models.CharField(max_length=30, choices=THEMES, default='One to watch"')
    releaseDate = models.DateField()


# class Image(models.Model):
#
#     def __str__(self):
#         return "{} for {}".format(self.name, self.product.name)
#
#     name = models.CharField(max_length=100)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='images/')
#     is_main = models.BooleanField(default=False)
