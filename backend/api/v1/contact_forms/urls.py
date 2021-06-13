from django.urls import path

from . import views


urlpatterns = [
    path("individual_project/add/", views.IndividualProjectRequestCreateAPIView.as_view()),
]