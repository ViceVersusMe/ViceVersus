from django.shortcuts import render_to_response, render
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from vice.models import Bounty, GiftCard, Pledge, Vice
from users.models import UserProfile


# class ViceList(ListView):
#     model = Vice
#     context_object_name = 'vice_list'
#     queryset = Vice.objects.all()
#     template_name = 'vicelist.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(ViceList, self).get_context_data(**kwargs)
#         return context


# def home(request):
#    context = RequestContext(request,
#                            {'user': request.user})
#    return render_to_response('home.html',
#                              context_instance=context)

def home(request):
   context = RequestContext(request,
                           {'request': request,
                            'user': request.user})
   return render_to_response('home.html',
                             context_instance=context)