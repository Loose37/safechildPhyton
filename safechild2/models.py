from django.db import models

class Students(models.Model):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  image = models.CharField(max_length=255)
  student_unique_ID = models.CharField(max_length=255)
  route = models.CharField(max_length=255)

  

