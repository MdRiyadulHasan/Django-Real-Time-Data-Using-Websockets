from django.db import models
from django.contrib.auth.models import User
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json


class Students(models.Model):
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    age = models.IntegerField()
    
    def __str__(self):
        return self.student_name



class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notification = models.TextField(max_length=250)
    is_seen = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Save the model instance first
        
        # Get the channel layer and construct the notification data
        channel_layer = get_channel_layer()
        notification_objs = Notification.objects.filter(is_seen=False).count()
        data = {'count': notification_objs, 'current_notification': self.notification}
        
        # Send the notification to the group
        async_to_sync(channel_layer.group_send)(
            'test-consumer-group', {
                'type': 'send_notification',
                'value': json.dumps(data)
            }
        )

        # super(Notification, self).save(*args, **kwargs)
       

    def __str__(self):
        return self.notification 

