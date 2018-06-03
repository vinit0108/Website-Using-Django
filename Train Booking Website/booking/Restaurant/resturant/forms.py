from django import forms

class RestForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100 )
    area = forms.CharField(label="Area", max_length=100)
    dishes = forms.CharField(label="Dishes", max_length=300, help_text="Write Dishes.",
                           widget=forms.Textarea)
    rating= forms.IntegerField(label="Rating", max_value=10)
