from django.urls import path, include

local_urlpatterns = [
    path('silk/', include('silk.urls', namespace='silk')),

]