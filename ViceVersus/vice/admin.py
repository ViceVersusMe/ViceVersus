from django.contrib import admin
from vice.models import Vice, GiftCard, Bounty, Pledge


@admin.register(Vice)
class ViceAdmin(admin.ModelAdmin):
    list_display = ('user', 'sponsor', 'created', 'end_date', 'strikes',)


@admin.register(GiftCard)
class GiftCardAdmin(admin.ModelAdmin):
    list_display = ('gift_card_name', 'gift_card_num', 'gift_card_value',
                    'bounty', 'pledge')


@admin.register(Bounty)
class BountyAdmin(admin.ModelAdmin):
    list_display = ('vice', 'collected', 'collected_by', 'busted_picture')


@admin.register(Pledge)
class PledgeAdmin(admin.ModelAdmin):
    list_display = ('user', 'vice')
