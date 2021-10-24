from django.urls import path
from .import views

urlpatterns=[
    path('home/',views.home,name='home'),
    path('signin/',views.signin,name='signin'),
    path('logout/',views.logout,name='logout'),
    path('visit/',views.visit,name='visit'),
    path('regist/',views.regist,name='regist'),
    path('explore/',views.explore,name='explore'),
    path('visitor/',views.visitor,name='visitor'),
    path('contact/',views.contactus,name='contact'),
    path('ticket/',views.ticket,name='ticket'),
    path('whatson/',views.whatson,name='whatson'),
]