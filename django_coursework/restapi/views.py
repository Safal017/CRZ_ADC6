from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from app.models import *
import json
@csrf_exempt
def view_put_delete_teacher(request,ID):
    if request.method == "PUT":
        teacher = Teacher.objects.get(id=ID)
        python_dictionary_object = json.loads(request.body)
        teacher.id= python_dictionary_object['id']
        teacher.first_name= python_dictionary_object['first_name']
        teacher.last_name= python_dictionary_object['last_name']
        teacher.email= python_dictionary_object['email']
        teacher.address= python_dictionary_object['address']
        teacher.subject =python_dictionary_object['subject']
        teacher.save()
        return JsonResponse({
            "message":"Updated Sucessfully!!"
        })
def api_student_pagination(request, PAGENO):
    SIZE = 5
    skip = SIZE * (PAGENO -1)
    student = Student.objects.all()[skip: PAGENO*SIZE]
    list_of_students = list(student.values('first_name','last_name','phone_no','address','student_class'))
    dictionary_name = {
        "student":list_of_students
    }
    return JsonResponse(dictionary_name)