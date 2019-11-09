from django.db import models

canisters = (
    ('1', 'Canister 1'),
    ('2', 'Canister 2'),
    ('3', 'Canister 3'),
    ('4', 'Canister 4'),
    ('5', 'Canister 5'),
    ('6', 'Not in cansister'),
)

class Reminder(models.Model):
    name = models.CharField(max_length=25)
    canister = models.ChoiceField(choices=canisters)
    time = models.TimeField()

