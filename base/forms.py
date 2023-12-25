# forms.py
from django import forms
from .models import UrlShortener

class UrlShortenerForm(forms.ModelForm):
    class Meta:
        model = UrlShortener
        fields = ['target_url', 'short_url']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add custom styling for validation errors if needed

    def clean_short_url(self):
        short_url = self.cleaned_data['short_url']
        if not short_url.isalnum():
            raise forms.ValidationError('Short URL can only contain letters and numbers.')
        return short_url
