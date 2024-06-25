from django.forms import EmailField, EmailInput, CharField, Textarea, TextInput
from django import forms
from .models import ContactModel
"""
size="30"
data-toggle="tooltip" title="Name is required"
class="form-control placeholder"
"""

class ContactForm(forms.Form):
    name = CharField(label='Name', widget=TextInput(attrs={
        'placeholder' : 'Name',
        'data-toggle' : 'tooltip',
        'class'       : 'form-control placeholder',
        'title'       : 'Name is required',
        'type'        : 'text',
        'name'        : 'Name',
        'id'          : 'name',
    }))
    email = EmailField(label='Email', widget=EmailInput(attrs={
        'placeholder' : 'Email',
        'data-toggle' : 'tooltip',
        'class'       : 'form-control placeholder',
        'title'       : 'Email is required',
        'type'        : 'email',
        'name'        : 'email',
        'id'          : 'email',
    }))
    subject = CharField(label='Subject', widget=TextInput(attrs={
        'placeholder' : 'Topic',
        'data-toggle' : 'tooltip',
        'class'       : 'form-control placeholder',
        'title'       : 'Subject is required',
        'type'        : 'text',
        'name'        : 'subject',
        'id'          : 'subject',
    }))
    message = CharField(label='Message', widget=Textarea(attrs={
        'placeholder' : 'Message',
        'data-toggle' : 'tooltip',
        'class'       : 'form-control placeholder',
        'title'       : 'Message is required',
        'rows'        : 4,
        'cols'        : 50,
        'name'        : 'message',
        'id'          : 'input-message',
    }))

    class Meta:
        model = ContactModel
        fields = ('user_email', 'subject', 'message','name')