from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from vice.models import Vice, GiftCard

class ViceForm(ModelForm):
    class Meta:
        model = Vice
        fields = ('user', 'sponsor', 'end_date',)

class GiftCardForm(ModelForm):
    class Meta:
        model = GiftCard
        fields = ('gift_card_name', 'gift_card_num', 'gift_card_value',)
