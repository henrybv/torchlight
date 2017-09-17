# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pprint
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect

from rest_framework.decorators import api_view, permission_classes, \
    renderer_classes

from .sms import send_sms, JOHN
from shelter.models import Person

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

class TestSmsView(TemplateView):
    def get(self, request, **kwargs):
    	result = send_sms(
    		text = request.GET.get('text', 'Oh jeez!'),
    		to = request.GET.get('to', JOHN),
		)

        return render(request, 'test_sms.html', context=dict(
        	result=result,
        	result_pretty=pprint.pformat(result),
        ))

class ShelterPageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'shelters.html', context=None)


@api_view(('POST',))
def PersonS(request):
    """
    record an event, all fields required
    {
        'origin': string,
        'action': string,
        'value': string
    }
    """
    
    person, created = Person.objects.update_or_create(
        name=request.POST.get('name', ''), defaults={"name": request.POST.get('name', ''),"phone":request.POST.get('phone', ''),"dob": request.POST.get('dob', '') }
)
    # obj, created = Person.objects.update_or_create(
    #     name=request.POST.get('name', ''),
    #     phone=request.POST.get('phone', ''),
    #     email=request.POST.get('email', ''),
    #     dob=request.POST.get('dob', ''),
    #     # defaults={
    #     #     'name': name, 'phone': phone,  'email': email, 'dob': dob,
    #     # }
    # )

    # obj, created = Person.objects.update_or_create(
    # # filter on the unique value of `upc`
    # upc=upc,
    # # update these fields, or create a new object with these values
    # defaults={
    #     'product_title': product_title, 'is_buyable': is_buyable,  'price': price, 
    #     'image_url': image_url, 'breadcrumb': breadcrumb, 'product_url': product_url,
    # }
# )

    # project  = Project.objects.get(title=offset)
    # date     = request.POST.get('date', '')
    # cost     = request.POST.get('cost', '')
    # cost_obj = Cost(project=project, date=date, cost=cost)
    # cost_obj.save()
    return HttpResponseRedirect('/')


    # to_extract = ['name', 'phone', 'dob']
    # required = to_extract
    # request, foreign_fields, errors = extract_fields(request, to_extract, required)

    # if errors:
    #     return Response(errors, status=status.HTTP_400_BAD_REQUEST)

    # # async_event(request, origin=foreign_fields['origin'], action=foreign_fields['action'],
    # #             value=foreign_fields['value'])
    # return Response()