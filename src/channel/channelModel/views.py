from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from channelModel.models import PpnCdmChannel
from channelModel.serializers import ChannelSerializer

@csrf_exempt
def channel_list(request):
    """
    List all channels, or create a new channel.
    """
    if request.method == 'GET':
        channels = PpnCdmChannel.objects.all()
        serializer = ChannelSerializer(channels, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ChannelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            # serializer.data 数据创建成功后所有数据
            return JsonResponse(serializer.data, status=201)
        # serializer.errors 错误信息
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def channel_detail(request, pk):
    """
    Retrieve, update or delete a code channel.
    """
    try:
        channel = PpnCdmChannel.objects.get(chan_id=pk)
    except PpnCdmChannel.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = ChannelSerializer(channel)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ChannelSerializer(channel, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        channel.delete()
        return HttpResponse(status=204)
