from django import forms


class FakeNewsForm(forms.Form):
    text = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}), label="Enter the news headline", label_suffix="")
