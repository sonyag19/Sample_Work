from django.urls import path
from .views import *
urlpatterns=[
   path('add/',add),
   path('sub/',sub),
   path('mul/',mul),
   path('div/',div),
   path('register/',register),
   path('register2/',register2),
   path('login/',login),
   path('search/',search),
   path('display/',display),
   path('display2/',display2),
   path('fileupload/',file),
   path('filedisplay/',filedisplay),
   path('header/',header),
   path('footer/',footer),
   path('index/',index),
   path('registrationbootstrap/',regboot),
   path('loginbootstrap/',loginboot),
   path('home/',home),
   path('card/',filedisplay)
]