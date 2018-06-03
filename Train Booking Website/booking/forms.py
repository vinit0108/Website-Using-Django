from django import forms

class BookingForm(forms.Form):
    source = forms.CharField(label="source", max_length=50,widget=forms.TextInput(
        attrs={
            'class' : 'form-control'
        }
    ))
    destination = forms.CharField(label="destination",max_length=50,widget=forms.TextInput(
        attrs={
            'class' : 'form-control'
        }
    ))
    date = forms.CharField(label="date", max_length=50,widget=forms.TextInput(
        attrs={
            'class' : 'form-control'
        }
    ))
    time = forms.CharField(label="time", max_length=50,widget=forms.TextInput(
        attrs={
            'class' : 'form-control'
        }
    ))
    adult = forms.CharField(label="adult", max_length=50,widget=forms.TextInput(
        attrs={
            'class' : 'form-control'
        }
    ))
    child = forms.CharField(label="child", max_length=50,widget=forms.TextInput(
        attrs={
            'class' : 'form-control'
        }
    ))
    age = forms.CharField(label="age", max_length=50,widget=forms.TextInput(
        attrs={
            'class' : 'form-control'
        }
    ))

class Filter(forms.Form):
    source = forms.CharField(label="Source", required=True,max_length=100)

    destination = forms.CharField(label="Destination", required=True, max_length=100)