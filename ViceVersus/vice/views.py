from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from vice.models import Bounty, GiftCard, Pledge, Vice
from users.models import UserProfile


class ViceList(ListView):
    model = Vice
    context_object_name = 'vice_list'
    queryset = Vice.objects.all()
    template_name = 'vicelist.html'

    def get_context_data(self, **kwargs):
        context = super(ViceList, self).get_context_data(**kwargs)
        return context
