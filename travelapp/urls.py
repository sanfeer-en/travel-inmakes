
from django.urls import path
from . import  views 

urlpatterns = [

    path('',views.demo,name = 'demo'),
    # path('add/',views.addition,name = 'about'),
    # path('contact/',views.contact,name = 'contact'),
    # path('thanks/',views.thanks,name = 'thanks'),
    # path('details/',views.details,name = 'details'),


]
