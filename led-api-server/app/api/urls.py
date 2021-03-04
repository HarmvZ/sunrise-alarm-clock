from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()
router.register("alarm-settings", views.AlarmConfigViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("status/", views.status_view),
    path("get_pixels/", views.get_pixels),
    path("set_color/", views.set_color),
    path("transition_color/", views.transition_color),
    path("show_clock/", views.show_clock),
    path("show_animation/", views.show_animation),
    path("start_alarm/<int:alarm_config_pk>/", views.start_alarm),
]
