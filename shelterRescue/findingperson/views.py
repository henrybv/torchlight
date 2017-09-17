# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pprint
from django.shortcuts import render
from django.views.generic import TemplateView

from .sms import send_sms, JADE

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

class TestSmsView(TemplateView):
    def get(self, request, **kwargs):
    	result = send_sms(
    		text = request.GET.get('text', 'Oh jeez!'),
    		to = request.GET.get('to', JADE),
		)

        return render(request, 'test_sms.html', context=dict(
        	result=result,
        	result_pretty=pprint.pformat(result),
        ))