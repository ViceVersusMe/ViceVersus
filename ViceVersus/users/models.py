from django.contrib.auth.models import User
from django.db import models



class UserProfile(models.Model):
    GENDERS = (
        ('male', 'Male'),
        ('female', 'Female')
    )
    user_name = models.OneToOneField(User)
    gender = models.CharField(max_length=20, null=True,
                              blank=True, choices=GENDERS)
    city = models.CharField(max_length=250, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    locale = models.CharField(max_length=10, null=True, blank=True)
    gift_cards = models.ForeignKey('vice.GiftCard')

    def __str__(self):
        return "{}, {}, {}, {}, {}".format(self.user_name, self.gender,
                                           self.city, self.dob,
                                           self.locale, self.gift_cards)

