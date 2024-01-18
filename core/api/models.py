from django.db import models
# Create your models here.
class Students(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.CharField(max_length=20)
    password=models.CharField(max_length=100)
    def __str__(self) :
        return self.user
# Create your models here.
