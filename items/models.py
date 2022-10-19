from email.policy import default
from django.db import models

# Create your models here.

class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"
    
    name = models.CharField(max_length=150)
    image = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Category: {self.name}"

class Item(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete = models.CASCADE,
        related_name="categories",
    )
    name = models.CharField(max_length=150)
    image = models.TextField()
    price = models.FloatField()
  

    def __str__(self):
        return self.name


class Comment(models.Model):
    items = models.ForeignKey(
        Item,
        on_delete = models.CASCADE,
        related_name = "comments",
    )
    
    message = models.TextField()
    def __str__(self) :
        return self.message