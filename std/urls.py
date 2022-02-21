from . import views
from django.urls import path
urlpatterns=[
    path('',views.home,name="hp"),
    path('cou',views.cos,name="co"),
    path('cns',views.con,name="cs")
    
]