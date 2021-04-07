import uuid
from urllib.request import urlopen

from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.db import models
from django.urls import reverse
from django.utils import timezone

class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    date = models.DateField(default=timezone.now,null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    text = models.TextField(max_length=2000, null=True, blank=True)
    # image = models.CharField(max_length=400, null=True, blank=True)
    # image = models.ImageField(upload_to='images', null=True)
    image_url = models.CharField(max_length=200,null=True)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f'{self.id}'

    def get_absolute_url(self):
        return reverse('item', args=[str(self.id)])

    # def save(self, *args, **kwargs):
    #     if self.image_url and not self.image:
    #         img_temp = NamedTemporaryFile(delete=True)
    #         img_temp.write(urlopen(self.image_url).read())
    #         img_temp.flush()
    #         self.image.save(f"image_{self.pk}", File(img_temp))
    #     super(Item, self).save(*args, **kwargs)

