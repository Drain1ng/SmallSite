from django import forms


class posForm(forms.Form):
    lat = forms.FloatField(label="latitude (deg)")
    lon = forms.FloatField(label="longititude (deg)")