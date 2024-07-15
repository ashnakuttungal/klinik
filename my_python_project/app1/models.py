from django.db import models


class doctordetails(models.Model):
    docname=models.CharField(max_length=200)
    docspecification=models.CharField(max_length=200)
    docemail=models.CharField(max_length=200)
    docphoto=models.ImageField()                   