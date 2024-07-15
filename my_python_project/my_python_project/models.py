from django.db import models

class Userdetailss(models.Model):
    username=models.CharField(max_length=200)
    useremail=models.CharField(max_length=200)
    usermobile=models.IntegerField()
    userpassword=models.CharField(max_length=200)
    
