from django import forms

class CollegeForm(forms.Form):
    # variable for the title of the product
    cid = forms.CharField(label="College id", max_length=100)
    # variable for the description of the product
    name = forms.CharField(label="College name", max_length=100)

    area = forms.CharField(label="Area", max_length=100)

    ratings = forms.CharField(label="Ratings", max_length=100)

    field = forms.CharField(label="Field", max_length=100)

