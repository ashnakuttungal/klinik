from django.db import models

# Create your models here.
class appointmentss(models.Model):
   u_id=models.CharField(max_length=12)
   ptname=models.CharField(max_length=200)
   ptemail=models.CharField(max_length=200)
   ptmobile=models.CharField(max_length=200)
   ptdoctor=models.CharField(max_length=200)
   ptdate=models.CharField(max_length=200)
   pttime=models.CharField(max_length=200)

    
