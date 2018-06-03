from django import forms

class EmployeForm(forms.Form):
    # variable for the title of the product
    title = forms.CharField(label="Employe id", max_length=100)
    # variable for the description of the product
    title1 = forms.CharField(label="Employe name", max_length=100)

    title2 = forms.CharField(label="Department", max_length=100)

    title3 = forms.CharField(label="Salary", max_length=100)

    title4 = forms.CharField(label="Date of birth", max_length=100)

    title5 = forms.CharField(label="Designation", max_length=100)