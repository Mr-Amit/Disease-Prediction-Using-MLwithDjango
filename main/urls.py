from django.urls import path
from . import views

urlpatterns = [
    #path('users/', views.home, name='home'),
    #path('', views.AjaxHandler.as_view()),
    path('', views.AjaxHandler.as_view() ,name = 'main'),
    # path('', views.home , name = 'home'),
]
