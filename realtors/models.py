from django.db import models
from datetime import datetime
#model files updated to trigger jenkins pipeline
class Realtor(models.Model):
    name=models.CharField(max_length=200)
    photo=models.ImageField(upload_to='photos/%y/%m/%d')
    discription=models.TextField()
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    is_mvp=models.BooleanField(default=False)
    hire_date=models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.name

# Create your models here.
