from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('black/', views.HomePageBlackView.as_view(), name='home_black'),
    path('4x/', views.HomePageView2.as_view(), name='home4'),
    path('5x/', views.HomePageView5.as_view(), name='home5'),
    path('6x/', views.HomePageView6.as_view(), name='home6'),
    path('7x/', views.HomePageView7.as_view(), name='home7'),
    path('8x/', views.HomePageView8.as_view(), name='home8'),
]