from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.FileField(upload_to='images/')
    
    def __str__(self):
        return str(self.name)