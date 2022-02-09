from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page, name='login'),
    path('page/', views.index, name='index'),
    path('index/', views.plcdata, name='plcdataa'),
    path('ELS/', views.KohliELS, name='els'),
    path('trial/', views.trials, name='trials')

]