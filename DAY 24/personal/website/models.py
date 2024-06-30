from django.db import models

# Create your models here.
class Detail(models.Model):
    name=models.CharField(max_length=255)
    mobile_number=models.BigIntegerField()
    address=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    image_url=models.CharField(max_length=1083)    
