# howdy/urls.py
from django.conf.urls import url
from shelter import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='index'),
     url(r'^shelters/$', views.ShelterPageView.as_view(), name='shelter_index'),
    url(r'^test_sms/$', views.TestSmsView.as_view(), name='test_sms'),
]