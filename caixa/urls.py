from django.conf.urls import url
from django.conf.urls import include
from caixa import views

urlpatterns = [    
    url(r'^$', views.lancamentos, name='index'),
]