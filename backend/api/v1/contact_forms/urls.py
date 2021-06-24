from django.urls import path

from . import views


urlpatterns = [
    path("individual_project/add/", views.IndividualProjectRequestCreateAPIView.as_view()),
    path("message/add/", views.MessageCreateAPIView.as_view()),
    path("consultation_reqeust/add/", views.ConsultationRequestCreateAPIView.as_view()),
    path("cooperation_application/add/", views.CooperationApplicationCreateAPIView.as_view()),
]