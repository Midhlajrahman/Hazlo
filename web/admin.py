from django.contrib import admin

from .models import (
    Contact,
    Faq,
    Gallery,
    Product,
    ProductFeatures,
    ProductImages,
    Testimonial,
    Updates,
)


# Register your models here.
class ProductFeaturesInline(admin.TabularInline):
    model = ProductFeatures
    fields = ("features",)
    extra = 1


class ProductImagesInline(admin.TabularInline):
    model = ProductImages
    fields = ("other_images",)
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("product_name",)
    inlines = [ProductFeaturesInline, ProductImagesInline]
    prepopulated_fields = {"slug": ("product_name",)}


@admin.register(Updates)
class UpdatesAdmin(admin.ModelAdmin):
    list_display = ("title",)
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ("name",)
