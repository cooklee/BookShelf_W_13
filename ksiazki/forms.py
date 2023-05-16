from django import forms
from django.core.exceptions import ValidationError

from ksiazki.models import Book


def check_if_malpa(value):
    if '@' not in value:
        raise ValidationError("małpa Musi być!!!")

def check_if_upper(value):
    if not value.istitle():
        raise ValidationError("Wielkimi!!!!")

class AddAuthorForm(forms.Form):
    first_name = forms.CharField(max_length=128, validators=[check_if_malpa, check_if_upper])
    last_name = forms.CharField(max_length=128)
    date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}), )



class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['author', 'publisher', 'year', 'title', 'categories']
        widgets = {
            'categories' : forms.CheckboxSelectMultiple
        }
