import re

from django import forms

from przychodnia_pacjent.models import Pacjent, Adres


class PacjentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PacjentForm, self).__init__(*args, **kwargs)
        self.fields["imie"].widget.attrs.update({"class": "form-control"})
        self.fields["nazwisko"].widget.attrs.update({"class": "form-control"})
        self.fields["adres"].widget.attrs.update({
            "class": "form-control select2-select"
        })
        self.fields["pesel"].widget.attrs.update(
            {
                "class": "form-control",
                "autocomplete": "off"
            }
        )

    def clean_pesel(self):
        pesel = self.cleaned_data['pesel']
        if not ( re.match("^[0-9]{11}$", pesel ) and 
        ( int(pesel[0]) * 1 + int(pesel[1]) * 3 + int(pesel[2]) * 7 + int(pesel[3]) * 9 
        + int(pesel[4]) * 1 + int(pesel[5]) * 3 + int(pesel[6]) * 7 + int(pesel[7]) * 9 
        + int(pesel[8]) * 1 + int(pesel[9]) * 3 + int(pesel[10]) * 1 ) % 10 == 0 ):
            raise forms.ValidationError("Podany format numeru PESEL jest nieprawidłowy")
        return pesel

    class Meta:
        model = Pacjent
        fields = ("imie", "nazwisko", "pesel", "adres")


class AdresForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AdresForm, self).__init__(*args, **kwargs)
        self.fields['miejscowosc'].widget.attrs.update({'class': 'form-control'})
        self.fields['ulica'].widget.attrs.update({'class': 'form-control'})
        self.fields['nr_domu'].widget.attrs.update({'class': 'form-control'})
        self.fields['nr_lokalu'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Adres
        fields = ("miejscowosc", "ulica", "nr_domu", "nr_lokalu")
