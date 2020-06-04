from django import forms
from .models import Contact


class ContactForms(forms.ModelForm):
    class Meta:
        model =  Contact
        fields = '__all__'

        widgets = {
            'name':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Add your name'
                }
            ),

            'lastName':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Add your Last name'
                }
            ),

            'email':forms.EmailInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Type your email'
                }
            ),

            'topic':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Type your topic'
                }
            ),

            'message':forms.Textarea(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Type your message'
                }
            ),

    }
