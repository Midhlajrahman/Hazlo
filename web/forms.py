from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ()

        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Your name:"}
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control required email",
                    "placeholder": "Your Mail:",
                }
            ),
            "subject": forms.TextInput(
                attrs={
                    "class": "form-control required",
                    "placeholder": "Enter Your Subject:",
                }
            ),
            "message": forms.Textarea(
                attrs={
                    "class": "form-control required",
                    "rows": 5,
                    "placeholder": "Your Massage:",
                }
            ),
        }
