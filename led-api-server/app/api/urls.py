from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()
router.register("alarm-settings", views.AlarmConfigViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("status/", views.status_view),
    path("start_alarm/<int:alarm_config_pk>/", views.start_alarm),
    path("stop_alarm/", views.stop_alarm),
]
