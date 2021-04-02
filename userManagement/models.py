import uuid
from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.db import models


class Token(models.Model):
    api_token = models.UUIDField(primary_key=True, default=uuid.uuid4, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(default=datetime.now() + timedelta(days=1), null=True)
