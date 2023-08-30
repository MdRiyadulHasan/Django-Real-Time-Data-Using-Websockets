from django.shortcuts import render
from channels.layers import get_channel_layer
from django.http import JsonResponse
from asgiref.sync import async_to_sync
import json, time
from .thread import *


# Create your views here.
async def home(request):
    channel_layer = get_channel_layer()
    for i in range(20):
        
        data = {"count":i}
        await (channel_layer.group_send)(
            'test-consumer-group',{
                'type':'send_notification1',
                'value':json.dumps(data)
            }
        )
   
    return render(request, 'mainApp/index.html')
def generate_student_data(request):
    total = request.GET.get('total')
    CreateStudentThread(int(total)).start()
    return JsonResponse({"status":200})
