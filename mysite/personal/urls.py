from django.conf.urls import url, include
from . import views
from personal.views import contact

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^thank-you/$', views.thankyou, name='thankyou'),

]
