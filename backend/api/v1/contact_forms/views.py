from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from backend.apps.contact_forms.models import IndividualProjectRequest
from .serializers import IndividualProjectRequestSerializer
from .services import send_notification


class IndividualProjectRequestCreateAPIView(CreateAPIView):
    """ Создание заявки на индивидуальный проект """
    queryset = IndividualProjectRequest.objects.none()
    serializer_class = IndividualProjectRequestSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        send_notification(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
