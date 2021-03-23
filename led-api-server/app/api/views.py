from alarms.models import AlarmConfig
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from alarms.utils.alarm_control_singleton import AlarmControlSingleton
from rest_framework import viewsets
from rest_framework.decorators import api_view

from api.serializers import AlarmConfigSerializer


@csrf_exempt
def status_view(request):
    return HttpResponse("", status=200)


@api_view(["POST"])
def start_alarm(request, alarm_config_pk):
    alarm_config = get_object_or_404(AlarmConfig, pk=alarm_config_pk)
    kwargs = AlarmConfigSerializer(alarm_config).data
    acs = AlarmControlSingleton()
    acs.start_alarm(**kwargs)
    return JsonResponse({"success": True}, status=200)


@api_view(["POST"])
def stop_alarm(request):
    acs = AlarmControlSingleton()
    acs.stop_alarm()
    return JsonResponse({"success": True}, status=200)


class AlarmConfigViewSet(viewsets.ModelViewSet):
    queryset = AlarmConfig.objects.all()
    serializer_class = AlarmConfigSerializer
