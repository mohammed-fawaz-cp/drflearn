from django.db import models

# Create your models here.
class Login(models.Model):
    name = models.CharField(max_length=120)
    phonenumber = models.IntegerField()
    password = models.IntegerField()

    @property
    def encoded_pass(self):
        return (self.password) +(self.password)