from django.db import models

# Create your models here.

class Piece(models.Model):

    title = models.CharField(max_length=500)
    description = models.CharField(max_length=2000,null=True,blank=True)
    year = models.CharField(max_length=4)

    height = models.IntegerField(null=True,blank=True)
    width = models.IntegerField(null=True,blank=True)
    depth = models.IntegerField(null=True,blank=True)

    image = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.title}"

