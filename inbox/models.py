from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class Mail(models.Model):
    sender = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name = 'sender')
    receiver = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name = 'receiver')
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=2000)
    send_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    arrive_date = models.DateTimeField(auto_now=False, auto_now_add=False)