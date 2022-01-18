from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('', views.AjaxHandler.as_view()),
    path('main/', views.AjaxHandler.as_view() ,name = 'main'),
    # path('', views.home , name = 'home'),
]
