from django.db import models

# Create your models here.
from django.db import models

class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    subject= models.CharField(max_length=50)
    
    def __str__(self): 
        return f"{self.first_name} {self.last_name} {self.email} {self.address} {self.subject}"

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    student_class= models.CharField(max_length=50)


    def __str__(self):
        return f"{self.first_name} , {self.last_name}, {self.address} , {self.student_class}"

 

    def is_valid_student(self):
        return (self.first_name !=self.last_name)and (self.phone_no != 0)

class Subject(models.Model):
    code =  models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    class_name= models.CharField(max_length=50)

    def __str__(self):
        return f"{self.code}, {self.name}, {self.class_name}"



class Class(models.Model):
    code = models.CharField(max_length=50)
    class_type = models.CharField(max_length=50)
    class_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.code},{self.class_type},{self.class_name}"


class Parents(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_no = models.IntegerField()
    address = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.first_name} , {self.last_name}, {self.address} " 

class Result(models.Model):
    student_id = models.IntegerField()
    student_name = models.CharField(max_length=50)
    subject_code = models.IntegerField()
    subject_name = models.CharField(max_length=50)
    teacher_name = models.CharField(max_length=50)
    marks_obtained = models.IntegerField()

    def __str__(self):
        return f"{self.student_name} , {self.teacher_name}, {self.subject_code} " 

class Assignment(models.Model):
    student_name = models.CharField(max_length=100, null=True, blank=True)
    document_name =models.CharField(max_length=100, null=True, blank=True)
    coursework_title = models.CharField(max_length=100, null=True, blank=True)
    pdf = models.FileField(upload_to='books/pdfs/')
    cover = models.ImageField(upload_to='books/covers/', null=True, blank=True)

