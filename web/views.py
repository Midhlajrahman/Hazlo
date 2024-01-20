from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from .forms import ContactForm
from .models import (
    Faq,
    Gallery,
    Product,
    ProductFeatures,
    ProductImages,
    Testimonial,
    Updates,
)


def index(request):
    products = Product.objects.all()
    features = ProductFeatures.objects.filter(product__in=products)
    updates = Updates.objects.all()[:3]
    testimonials = Testimonial.objects.all()

    context = {
        "products": products,
        "features": features,
        "updates": updates,
        "testimonials": testimonials,
    }
    return render(request, "web/index.html", context)


def about(request):
    faqs = Faq.objects.all()
    testimonials = Testimonial.objects.all()
    context = {
        "testimonials": testimonials,
        "faqs": faqs,
    }
    return render(request, "web/about.html", context)


def products(request):
    products = Product.objects.all()
    features = ProductFeatures.objects.filter(product__in=products)
    images = ProductImages.objects.filter(product__in=products)

    context = {"products": products, "features": features, "images": images}
    return render(request, "web/products.html", context)


def product_details(request, slug):
    other_products = Product.objects.exclude(slug=slug)
    product = get_object_or_404(Product, slug=slug)
    features = ProductFeatures.objects.filter(product=product)

    context = {
        "product": product,
        "features": features,
        "other_products": other_products,
    }

    return render(request, "web/product_details.html", context)


def blog(request):
    updates = Updates.objects.all()
    context = {
        "updates": updates,
    }
    return render(request, "web/blog.html", context)


def update_details(request, slug):
    update = get_object_or_404(Updates, slug=slug)
    other_updates = Updates.objects.exclude(slug=slug)
    context = {
        "update": update,
        "other_updates": other_updates,
    }
    return render(request, "web/update_details.html", context)


def gallery(request):
    gallerys = Gallery.objects.all()
    context = {
        "gallerys": gallerys,
    }
    return render(request, "web/gallery.html", context)


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            response_data = {
                "status": "true",
                "title": "Successfully Submitted",
                "message": "Thank You, Our Team Will Contact You Soon",
            }
        else:
            error_messages = {field: form.errors[field][0] for field in form.errors}
            print("Form Validation Error:", error_messages)  # Print the errors
            response_data = {
                "status": "false",
                "title": "Form Validation Error",
                "message": error_messages,
            }
        return JsonResponse(response_data)
    else:
        form = ContactForm()
        context = {"form": form, "is_contact": True}
        return render(request, "web/contact.html", context)
