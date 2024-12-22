from django.urls import path

from .import views


urlpatterns=[
    path('',views.hhome,name='loginpage'),
    path('login/',views.login,name='loginpage'),
    path('home/',views.home,name='homepage'),
    path('login/',views.hh,name='page'),
    path('login/',views.hhh,name='page'),
    path('home/',views.hhome,name='hhomepage'),
    path('registration/',views.registration,name='registerpage'),
    path('saveuser/',views.saveuser),
    path('verifyuser/',views.verifyuser),
    path('result/',views.result)
]