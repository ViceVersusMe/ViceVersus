from django.db import models


class Vice(models.Model):
    user = models.ForeignKey('users.UserProfile')
    sponsor = models.ForeignKey('users.UserProfile', related_name='sponsor')
    created = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    strikes = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return "{}, {}, {}, {}, {}".format(self.user, self.sponsor,
                                           self.created, self.end_date,
                                           self.strikes)


class Bounty(models.Model):
    vice = models.ForeignKey(Vice)
    collected = models.BooleanField(default=False)
    collected_by = models.ForeignKey('users.UserProfile', default=None)
    busted_picture = models.ImageField()

    def __str__(self):
        return "{}, {}, {}, {}, {}".format(self.vice,
                                           self.amount,
                                           self.collected,
                                           self.collected_by,
                                           self.busted_picture)


class Pledge(models.Model):
    user = models.ForeignKey('users.UserProfile')
    vice = models.ForeignKey(Vice)

    def all_pledges(self):
        pledges = Pledge.objects.all(pk=self.vice_id)
        return pledges

    def __str__(self):
        return "{}, {}".format(self.user, self.vice)


class GiftCard(models.Model):
    DENOMINATION = (
        ('25', '$25.00'), ('50', '$50.00'), ('75', '$75.00'),
        ('100', '$100.00'), ('125', '$125.00'), ('150', '$150.00'),
        ('175', '$175.00'), ('200', '$200.00'), ('225', '$225.00'),
        ('250', '$250.00'), ('275', '$275.00'), ('300', '$300.00')
    )
    gift_card_name = models.CharField(max_length=250)
    gift_card_num = models.CharField(max_length=100)
    gift_card_value = models.DecimalField(max_digits=8, decimal_places=2,
                                          choices=DENOMINATION)
    bounty = models.ForeignKey(Bounty)
    pledge = models.ForeignKey(Pledge)

    def pledge_gift_card(self):
        pledge_card = GiftCard.objects.get(pk=self.pledge.user.id)
        return pledge_card

    def bounty_gift_card(self):
        bounty_card = GiftCard.objects.get(pk=self.bounty.vice.user.id)
        return bounty_card

    def pledge_sum(self):
        pledge_sum = GiftCard.objects.all(pk=self.pledge.vice_id).aggregate(sum('gift_card_value'))
        return pledge_sum

    def bounty_sum(self):
        bounty_sum = GiftCard.objects.all(pk=self.bounty.vice_id).aggregate(sum('gift_card_value'))
        return bounty_sum

    def __str__(self):
        return "{}, {}, {}".format(self.gift_card_name,
                                   self.gift_card_num,
                                   self.gift_card_value,
                                   self.bounty,
                                   self.pledge)
