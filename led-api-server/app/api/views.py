from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from alarms.models import AlarmConfig
from api.serializers import (
    ColorSerializer,
    TransitionColorSerializer,
    ClockSerializer,
    AnimationSerializer,
    AlarmConfigSerializer,
)
from api.utils import bit24_to_3_bit8
from api.zmq_client import ZMQClient


@csrf_exempt
def status_view(request):
    return HttpResponse("", status=200)


@api_view(["GET"])
def get_pixels(request):
    zmqc = ZMQClient()
    pixels = zmqc.perform_request("get_pixels")
    pixels_rgb = [bit24_to_3_bit8(c) for c in pixels]
    return JsonResponse({"pixels": pixels_rgb}, status=200)


def abstract_view(request, fn_name, Serializer, kwarg_keys=[]):
    success = False
    serializer = Serializer(data=request.data)
    if serializer.is_valid():
        kwargs = {}
        for kwarg_key in kwarg_keys:
            kwargs.update({kwarg_key: serializer.data[kwarg_key]})
        zmqc = ZMQClient()
        zmqc.perform_request(fn_name, **kwargs)
        success = True
    status = 200 if success else 400
    data = {"success": success}
    if not success:
        data.update({"errors": serializer.errors})

    return JsonResponse(data, status=status)


@api_view(["POST"])
def set_color(request):
    return abstract_view(request, "fill", ColorSerializer, ["r", "g", "b"])


@api_view(["POST"])
def transition_color(request):
    return abstract_view(
        request,
        "transition_to_color",
        TransitionColorSerializer,
        ["r", "g", "b", "steps", "timestep"],
    )


@api_view(["POST"])
def show_clock(request):
    return abstract_view(request, "show_time", ClockSerializer, ["fg", "bg"])


@api_view(["POST"])
def show_animation(request):
    return abstract_view(
        request, "animation", AnimationSerializer, ["animation", "wait_ms"]
    )


@api_view(["POST"])
def start_alarm(request, alarm_config_pk):
    alarm_config = get_object_or_404(AlarmConfig, pk=alarm_config_pk)
    kwargs = AlarmConfigSerializer(alarm_config).data
    zmqc = ZMQClient()
    zmqc.perform_request("start_alarm", **kwargs)
    return JsonResponse({"success": True}, status=200)


class AlarmConfigViewSet(viewsets.ModelViewSet):
    queryset = AlarmConfig.objects.all()
    serializer_class = AlarmConfigSerializer
