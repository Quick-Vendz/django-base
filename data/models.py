from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True)
    color = models.CharField(max_length=10, default="neutral")

    def __str__(self):
        return self.name
