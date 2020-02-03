from django import forms
from virus_form.models import States


class DeathForm(forms.Form):
    """the form that will take the data of the death"""
    state_obj = States.objects.all()
    list_comp = []
    list_comp2 = []
    for state in state_obj:
        list_comp += [state.state]
        list_comp2 += [state.state]
    zip_tup = zip(list_comp, list_comp2)
    states = forms.ChoiceField(choices=zip_tup)
    death_count = forms.CharField(max_length=80, label='Submit Deaths')
