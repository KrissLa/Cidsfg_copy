from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('black/', views.HomePageBlackView.as_view(), name='home_black'),
    path('075s/', views.HomePage075View.as_view(), name='home_black'),
    path('1s/', views.HomePage1View.as_view(), name='home_black'),
    path('4x/', views.HomePageView2.as_view(), name='home4'),
]