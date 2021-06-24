from django.urls import path

from . import views


urlpatterns = [
    path("individual_project/add/", views.IndividualProjectRequestCreateAPIView.as_view()),
    path("message/add/", views.MessageCreateAPIView.as_view()),
]