from django.db import models
import os
import uuid
from django.contrib.auth.models import User


class Student(models.Model):
    Id=models.AutoField(primary_key=True)
    StudentId=models.CharField(max_length=10)
    Firstname=models.CharField(max_length=50)
    Lastname=models.CharField(max_length=50)
    Middlename=models.CharField(max_length=50) 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.StudentId

class ExaminationMain(models.Model):
    Id=models.AutoField(primary_key=True)
    ExaminationId=models.CharField(max_length=10) 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ExaminationId

class ExaminationDetails(models.Model):
    Id=models.AutoField(primary_key=True)
    ExaminationMain=models.CharField(max_length=250) 
    Student=models.ForeignKey(Student, on_delete=models.CASCADE)
    StudentIdNo=models.CharField(max_length=50)
    Fullname=models.CharField(max_length=250,default="") 
    #students = models.ManyToManyField(Student, related_name="examMain")
    # students = models.ManyToManyField(Student,related_name='examinee') 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ExaminationId

class answerKey(models.Model):
    Id=models.AutoField(primary_key=True)
    ExaminationId=models.CharField(max_length=250) 
    Item=models.IntegerField()
    Answer=models.CharField(max_length=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.ExaminationId  


class uploadAnswerSheet(models.Model):
    image = models.ImageField(upload_to='uploads/', null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.image:
            # Get the file extension
            ext = self.image.name.split('.')[-1]
            # Generate a new file name
            new_filename = f"{uuid.uuid4()}.{ext}"
            # Set the new file name
            self.image.name = os.path.join('uploads/', new_filename)
        super().save(*args, **kwargs)

class examResult(models.Model):
    Id=models.AutoField(primary_key=True)
    ExaminationId=models.CharField(max_length=250) 
    StudentIdNo=models.CharField(max_length=50)
    Fullname=models.CharField(max_length=250) 
    Items=models.IntegerField()
    Score=models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ExaminationId

