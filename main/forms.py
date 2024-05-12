from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super(ContactForm, self).clean()

    class Meta:
        model = Contact
        fields = ('name', 'email', 'tel', 'message')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name', 'placeholder': 'Your Name *'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'email', 'placeholder': 'Your Email *'}),
            'tel': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Phone *'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'id': 'message', 'placeholder': 'Your Message *'}),
        }
        labels = {'name':'name','email':'email','tel':'tel','message':'message'}
        help_texts = {'Input a valid phone number'}
        error_messages = {
            'name': { 'required': 'This field is required.'},
            'email': { 'required': 'This field is required.'},
            'tel': { 'required': 'This field is required.'},
            'message': { 'required': 'This field is required.'},

        }