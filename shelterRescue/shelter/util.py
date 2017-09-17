from dateutil import parser
from datetime import datetime, timedelta
from HTMLParser import HTMLParser
import logging
import time

from rest_framework.response import Response

def extract_fields(request, to_extract, required):
    """Return extracted fields from request.data as a dict.

    REST Framework is bad at writing to nested models so we'll pull all
    foreign fields from request.data and deal with them separately
    """

    foreign_fields = {}
    errors = {}
    for field in to_extract:
        if field in request.data:
            foreign_fields[field] = request.data.get(field)
            try:
                del request.data[field]
            except AttributeError:
                pass
        elif field in required:
            error = '{0} is a required field.'.format(field)
            errors[field] = error
    return request, foreign_fields, errors

def extract_fields_from_GET(request, to_extract, required):
    """Return extracted fields from request.GET as a dict."""
    foreign_fields = {}
    errors = {}
    for field in to_extract:
        if field in request.GET:
            foreign_fields[field] = request.GET.get(field)
        elif field in required:
            error = '{0} is a required field.'.format(field)
            errors[field] = error
    return request, foreign_fields, errors
