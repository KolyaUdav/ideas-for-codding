from django import forms

class AddIdeaForm(forms.Form):
    ideaTitle = forms.CharField(label='Название', min_length=3, max_length=30)
    ideaText = forms.CharField(label='Описание', min_length=5, max_length=200)