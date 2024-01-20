from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_image = models.ImageField(upload_to="product/")
    price = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.product_name)
        super(Product, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("web:product_details", kwargs={"slug": self.slug})

    def __str__(self):
        return self.product_name


class ProductFeatures(models.Model):
    product = models.ForeignKey(
        "web.Product", on_delete=models.CASCADE, blank=True, null=True
    )
    features = models.CharField(max_length=200)


class ProductImages(models.Model):
    product = models.ForeignKey(
        "web.Product", on_delete=models.CASCADE, blank=True, null=True
    )
    other_images = models.ImageField(upload_to="product/")


class Updates(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="updates/")
    description = models.TextField()
    date = models.DateField()
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Updates, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("web:update_details", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    image = models.ImageField(upload_to="testimonial/")
    title = models.CharField(max_length=200)
    description = models.TextField()
    name = models.CharField(max_length=100, blank=True)
    position = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=300)
    message = models.TextField()

    def __str__(self):
        return self.name


class Faq(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class Gallery(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to="gallery/")

    def __str__(self):
        return self.name
