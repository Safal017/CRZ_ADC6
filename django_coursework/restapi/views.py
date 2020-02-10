from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from app.models import *
import json
# Create your models here.
@csrf_exempt
def view_get_post_teacher(request):
    if request.method == "GET":
        teacher = Teacher.objects.all()
        list_of_teacher = list(teacher.values("id","first_name","last_name","email","address","subject"))
        dictionary_name = {
        "teacher":list_of_teacher
    }
        return JsonResponse(dictionary_name)
        
    elif request.method == "POST":
        python_dictionary_object = json.loads(request.body)
        Teacher.objects.create(id=python_dictionary_object['id'],first_name=python_dictionary_object['first_name'],last_name=python_dictionary_object['last_name'],email=python_dictionary_object['email'],address=python_dictionary_object['address'],subject=python_dictionary_object['subject'])
        return JsonResponse({
            "message":"Successfully posted!!"
        })
    else:
        return HttpResponse("Other HTTP verbs testing")

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
    elif request.method == "DELETE":
        teacher= Teacher.objects.get(id=ID)
        teacher.delete()     
        return JsonResponse({
            "message":"Deleted Sucessfully! !"
        }) 
    else:
        return HttpResponse("Error")
        
@csrf_exempt 
def view_get_post_student(request):
    if request.method == "GET":
        student = Student.objects.all()
        list_of_student = list(student.values("first_name","last_name","phone_no","address","student_class"))
        dictionary_name = {
        "student":list_of_student
    }
        return JsonResponse(dictionary_name)
        
    elif request.method == "POST":
        python_dictionary_object = json.loads(request.body)
        Student.objects.create(first_name=python_dictionary_object['first_name'],last_name=python_dictionary_object['last_name'],phone_no=python_dictionary_object['phone_no'],address=python_dictionary_object['address'],student_class=python_dictionary_object['student_class'])
        return JsonResponse({
            "message":"Successfully posted!!"
        })
    else:
        return HttpResponse("Other HTTP verbs testing")
        
@csrf_exempt 
def view_get_post_subject(request):
    if request.method == "GET":
        subject =Subject.objects.all()
        list_of_subject = list(subject.values("code","name","class_name"))
        dictionary_name = {
        "subject":list_of_subject
    }
        return JsonResponse(dictionary_name)
        
    elif request.method == "POST":
        python_dictionary_object = json.loads(request.body)        
        Subject.objects.create(code=python_dictionary_object['code'],name=python_dictionary_object['name'],class_name=python_dictionary_object['class_name'])
        return JsonResponse({
            "message":"Successfully posted!!"
        })
    else:
        return HttpResponse("Other HTTP verbs testing")

        
@csrf_exempt 
def view_get_post_class(request):
    if request.method == "GET":
        classes =Class.objects.all()
        list_of_classes = list(classes.values("code","class_type","class_name"))
        dictionary_name = {
        "classes":list_of_classes
    }
        return JsonResponse(dictionary_name)
        
    elif request.method == "POST":
        python_dictionary_object = json.loads(request.body)      
        Class.objects.create(code=python_dictionary_object['code'],class_type=python_dictionary_object['class_type'],class_name=python_dictionary_object['class_name'])
        return JsonResponse({
            "message":"Successfully posted!!"
        })
    else:
        return HttpResponse("Other HTTP verbs testing")

        
@csrf_exempt 
def view_get_post_parents(request):
    if request.method == "GET":
        parents = Parents.objects.all()
        list_of_parents = list(parents.values("first_name","last_name","phone_no","address"))
        dictionary_name = {
        "parents":list_of_parents
    }
        return JsonResponse(dictionary_name)
        
    elif request.method == "POST":
        python_dictionary_object = json.loads(request.body) 
        Parents.objects.create(first_name=python_dictionary_object['first_name'],last_name=python_dictionary_object['last_name'],phone_no=python_dictionary_object['phone_no'],address=python_dictionary_object['address'])
        return JsonResponse({
            "message":"Successfully posted!!"
        })
    else:
        return HttpResponse("Other HTTP verbs testing")


          
@csrf_exempt       
def view_parents_getByID_updateByID_deleteByID(request,ID):
    if request.method == "GET":
        parent= Parents.objects.get(id = ID)
        return JsonResponse({
            "id":parent.id,
            "first_name":parent.first_name,
            "last_name":parent.last_name,
            "phone_no":parent.phone_no,
            "address":parent.address,
            "student":parent.student,
        })
    else:
        return JsonResponse({
        "message":" Other htpp verbs Testing"
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