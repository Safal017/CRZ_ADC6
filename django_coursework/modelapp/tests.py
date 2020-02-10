from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import *
from django.contrib.auth.models import User

# Create your tests here.
class ModelTestCase(TestCase):
    def test_is_valid_student(self):
        t1 = Teacher.objects.create(first_name="Raj ",last_name="Prasad Shrestha",email="r1@gmail.com",address="Chabhil",subject="Computer Science")
        s1 = Student.objects.create(first_name="Niraj",last_name="Khadka",details=t1,phone_no=9822445533,address="Chabhil,Kathmandu",student_class="Class 10")
        self.assertTrue(s1.is_valid_student())

    def test_is_valid_teacher(self):
        tec = Teacher.objects.create(first_name="Raj ",last_name="Prasad Shrestha",email="r1@gmail.com",address="Chabhil",subject="Computer Science")
        value=tec.is_valid_teacher()
        self.assertEqual(value,True)

    def test_is_valid_class(self):
        t1 = Teacher.objects.create(first_name="Raj ",last_name="Prasad Shrestha",email="r1@gmail.com",address="Chabhil",subject="Computer Science")
        s1 = Student.objects.create(first_name="Niraj",last_name="Khadka",details=t1,phone_no=9822445533,address="Chabhil,Kathmandu",student_class="Class 10")
        cl = Class.objects.create(code="A1",student=s1)
        self.assertTrue(cl.is_valid_class())

    def test_is_valid_parents(self):
        t1 = Teacher.objects.create(first_name="Raj ",last_name="Prasad Shrestha",email="r1@gmail.com",address="Chabhil",subject="Computer Science")
        s1 = Student.objects.create(first_name="Niraj",last_name="Khadka",details=t1,phone_no=9822445533,address="Chabhil,Kathmandu",student_class="Class 10")
        p1 = Parents.objects.create(first_name="Rajendra",last_name="Khadka",phone_no=9855446611,address="Fattepur,Saptari",student=s1)
        value = p1.is_valid_parents()
        self.assertEqual(value,True)
    
    def test_is_valid_studentlist(self):
        s1 = Student.objects.create(first_name="Niraj",last_name="Khadka",phone_no=9822445533,address="Chabhil,Kathmandu")
        self.assertTrue(s1.is_valid_student())