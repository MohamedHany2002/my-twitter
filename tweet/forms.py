from django import forms
from .models import Tweet

class tweetForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows':2,'place-holder':'Create new tweet','id':'text_tweet'}))
    class Meta:
        model=Tweet
        fields=['text']
    def clean_text(self):
        text=self.cleaned_data['text']
        if text == 'lol':
            return forms.ValidationError("can't be lol")
        return text
    