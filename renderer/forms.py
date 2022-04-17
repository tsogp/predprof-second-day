from django import forms


class AnomalyForm(forms.Form):
    dec_id = forms.CharField(max_length=100)
    dec_x = forms.FloatField()
    dec_y = forms.FloatField()