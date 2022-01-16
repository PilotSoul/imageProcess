from django.db import models


class ImageP(models.Model):
    image = models.ImageField(upload_to='')
