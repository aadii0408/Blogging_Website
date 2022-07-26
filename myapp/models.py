from django.db import models

# Create your models here.

class Student(models.Model):
    sId = models.CharField(max_length = 10)
    sName = models.CharField(max_length=30)
    sEmail = models.EmailField()
    sPassword = models.CharField(max_length=20)

class Blog(models.Model):
    user_id = models.ForeignKey(Student,on_delete=models.CASCADE)
    #for breaking dependancy(in table)->on_delete
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to="image/")  #for image we have to install lib. pillow
    postDetail = models.CharField(max_length=300)
    publisherName = models.CharField(max_length=30)
