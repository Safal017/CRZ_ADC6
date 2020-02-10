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

    def is_valid_teacher(self):
        return (self.first_name!=self.last_name)

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    details = models.ForeignKey(Teacher,on_delete=models.CASCADE,related_name="teacher",null=True)
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
    student = models.ManyToManyField(Student,blank=True)

    def __str__(self):
        return f"{self.code}, {self.name}{self.student} {self.class_name}"



class Class(models.Model):
    code = models.CharField(max_length=50)
    class_type = models.CharField(max_length=50)
    class_name = models.CharField(max_length=50)
    student = models.ForeignKey(Student,on_delete=models.CASCADE,related_name="student",null=True)

    def __str__(self):
        return f"{self.code}{self.class_type}{self.class_name}"

    def is_valid_class(self):
        return (self.code !=self.student)

class Parents(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_no = models.IntegerField()
    address = models.CharField(max_length=50)
    student = models.OneToOneField(Student,on_delete=models.CASCADE,related_name="students",null=True)
    
    def __str__(self):
        return f"{self.first_name} , {self.last_name}, {self.address} " 

    def is_valid_parents(self):
        return (self.first_name !=self.last_name)

