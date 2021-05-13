from django.urls import path

from . import views

urlpatterns = [
    # path("", views.HouseListAPIView.as_view()),
    path("add_consultation_reqeust/", views.ConsultationRequestCreateAPIView.as_view()),
]
