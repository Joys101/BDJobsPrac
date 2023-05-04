from django import forms
from .models import book

class BookForm(forms.ModelForm):
    class Meta:
        model = book
        fields = ['title', 'publisher', 'age', 'page_count', 'publish_date', 'book_type']