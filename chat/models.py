from django.db import models

# Create your models here.
class Chat(models.Model):
    name = models.CharField(max_length=120)
    phonenumber = models.IntegerField()
    message = models.TextField()
    time = models.DateTimeField(default=None)
    def __str__(self):
        return self.name