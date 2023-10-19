from django.db import models

# Create your models here.
class table1(models.Model):
    name = models.CharField(max_length=220)
    img = models.ImageField(upload_to="my_pics")
    desc = models.TextField()

    def __str__(self):
        return self.name

class table2(models.Model):
    fullname = models.CharField(max_length=200)
    pic = models.ImageField(upload_to='my_pics')

    def __str__(self):
        return self.fullname
