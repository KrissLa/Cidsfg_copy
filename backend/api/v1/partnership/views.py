from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from backend.partnership.models import CooperationApplication
from .serializers import CooperationApplicationSerializer
from .services import send_notification


class CooperationApplicationCreateAPIView(CreateAPIView):
    """ Добавление сообщения """
    queryset = CooperationApplication.objects.none()
    serializer_class = CooperationApplicationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        send_notification(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
