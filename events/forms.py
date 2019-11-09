from django import forms
from django.forms import inlineformset_factory


class ReminderForm(forms.Form):
    class Meta:
        model = Reminder
        exclude = ()

ReminderFormset = inlineformset_factory(ReminderForm, extra=1)
