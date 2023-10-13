from django.db import models

class Cloud(models.Model):
    ip = models.CharField(max_length=200)
    common_name = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    country = models.CharField(max_length=50)
    locality = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    sandns =  models.TextField()
    sanip = models.TextField()
    selfsigned = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name
