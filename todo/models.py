from django.db import models

# Create your models here.
class task(models.Model):
    item = models.CharField(max_length=50)
    completed = models.BooleanField(default=False)
    catagory = models.CharField(max_length=20,default='all_item')
    
    def __str__(self):
        return self.item