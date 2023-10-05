from django.db import models

# Create your models here.
class User(models.Model):
    No=models.PositiveBigIntegerField()
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    DOB=models.DateField()
    address=models.CharField(max_length=50)


    def __str__(self):
        return f'User: {self.first_name} {self.last_name}'



