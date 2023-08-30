import threading
from faker import Faker
fake = Faker()
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json
import time
import random
from . models import *

class CreateStudentThread(threading.Thread):
    
    def __init__(self , total):
        self.total = total
        threading.Thread.__init__(self)
    
    def run(self):
        try:
            print("Starting CreateStudent Thread")
            channel_layer = get_channel_layer()
            current_total = 0
            for i in range(self.total):
                current_total +=1
                student_obj = Students.objects.create(
                    student_name = fake.name(),
                    student_email = fake.email(),
                    address  = fake.address(),
                    age = random.randint(10,60)

                )
                data = {
                    "id":current_total,
                    "total": self.total,
                    "current_total": current_total,
                    "name":student_obj.student_name,
                    "email": student_obj.student_email,
                    "address": student_obj.address,
                    "age": str(student_obj.age)

                }
                # print(data)
                async_to_sync (channel_layer.group_send)(
                    'test-consumer-group',{
                        'type':'send_notification1',
                        'value':json.dumps(data)
                    }
                )
        except Exception as e:
            print(e)