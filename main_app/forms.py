from django import forms
from main_app.models import ContactMessage

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['fullname', 'phone_number', 'email', 'message']


