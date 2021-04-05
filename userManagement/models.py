import uuid
from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


def return_date_time():
    now = timezone.now()
    return now + timedelta(days=1)

class Token(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    api_token = models.UUIDField(default=uuid.uuid4, null=False)
    date = models.DateTimeField(default=return_date_time, null=True)
