from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    img_cat = models.ImageField(upload_to='category', blank=True, null=True, default='default.jpg')
    slug = models.SlugField(unique=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', args=[str(self.slug)])


class Marques(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    logo = models.ImageField(upload_to='marques/', null=True, blank=True)
    slug = models.SlugField(unique=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Marques, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Appareils(models.Model):
    name = models.CharField(max_length=255)
    marque = models.ForeignKey(Marques, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='devices/', null=True, blank=True)
    slug = models.SlugField(unique=True, editable=False)
    duree = models.DateTimeField(auto_now_add=False, auto_now=False, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Appareils, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
