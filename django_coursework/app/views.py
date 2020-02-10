from django.shortcuts import *
from django.db.models import *
# Create your views here.
from django.shortcuts import *
from django.http import HttpResponse
from .models import *


def view_home_page(request):
    return render(request,'index.html')

def view_students_lists(request):
    list_of_students= Student.objects.all()

    context_variable = {
        'student':list_of_students
    }
    return render(request,'students/students_list.html',context_variable)

def view_students_list_page(request):
    return render(request,'students/students_list.html')

def view_student_form(request):
    return render(request,'students/student_form.html')

def view_studentdata_save(request):
    if request.method == "POST":
        get_all = request.POST
        get_first_name = request.POST['first_name']
        get_last_name = request.POST['last_name']
        get_phone_no = request.POST['phone_no']
        get_address = request.POST['address']
        students_obj = Student(first_name=get_first_name,last_name=get_last_name,phone_no=get_phone_no,address=get_address)
        students_obj.save()
        return redirect('/app/studentlist/')
    else:
        return HttpResponse("Error record saving")


def view_Studentdata_updateform(request,ID):
    students_obj = Student.objects.get(id=ID)
    context_varible = {
        'students': students_obj
    }
    return render(request,'students/update_student.html',context_varible)

def view_student_update_form_data_in_db(request,ID):
    students_obj = Student.objects.get(id=ID)
    student_form_data = request.POST
    students_obj.first_name = request.POST['first_name']
    students_obj.last_name = request.POST['last_name']
    students_obj.phone_no = request.POST['phone_no']
    students_obj.address = request.POST['address']
    students_obj.save()
    return redirect('/app/studentlist/')

def deletestudent(request, ID):
    studentobj = Student.objects.get(id=ID)
    studentobj.delete()
    return redirect('/app/studentlist/')


def search(request):
    if request.method=='POST':
        srch = request.POST['search']

        if srch:
            match = Student.objects.filter(
                Q(first_name__icontains=srch) | Q(address__icontains=srch)
                )

            if match:
                return render(request,'students/search_student.html', {'src':match})

            else:
                return HttpResponse('Result Not Found')
        else:
            return HttpResponseRedirect('/app/searchstudent/')

    return render(request,'students/search_student.html')




def view_teacher_lists(request):
    list_of_teachers= Teacher.objects.all()

    context_variable = {
        'teacher':list_of_teachers
    }
    return render(request,'teacher/teacher_list.html',context_variable)

def view_teachers_list_page(request):
    return render(request,'teacher/teacher_list.html')

def view_teacher_form(request):
    return render(request,'teacher/teacher_form.html')

def view_teacherdata_save(request):
    if request.method == "POST":
        get_all = request.POST
        get_first_name = request.POST['first_name']
        get_last_name = request.POST['last_name']
        get_email = request.POST['email']
        get_address = request.POST['address']
        get_subject= request.POST['subject']
        teacher_obj = Teacher(first_name=get_first_name,last_name=get_last_name,email=get_email,address=get_address,subject=get_subject)
        teacher_obj.save()
        return redirect('/app/teacherlist/')
    else:
        return HttpResponse("Error record saving")


def view_teacherdata_updateform(request,ID):
    teacher_obj = Teacher.objects.get(id=ID)
    context_varible = {
        'teachers': teacher_obj
    }
    return render(request,'teacher/update_teacher.html',context_varible)

def view_teacher_update_form_data_in_db(request,ID):
    teacher_obj = Teacher.objects.get(id=ID)
    teacher_form_data = request.POST
    teacher_obj.first_name = request.POST['first_name']
    teacher_obj.last_name = request.POST['last_name']
    teacher_obj.email = request.POST['email']
    teacher_obj.address = request.POST['address']
    teacher_obj.subject = request.POST['subject']
    teacher_obj.save()
    return redirect('/app/teacherlist/')

def deleteteacher(request, ID):
    teacherobj = Teacher.objects.get(id=ID)
    teacherobj.delete()
    return redirect('/app/teacherlist/')

def searchteacher(request):
    if request.method=='POST':
        srch = request.POST['search']

        if srch:
            match = Teacher.objects.filter(
                Q(first_name__icontains=srch) | Q(email__icontains=srch)
                )

            if match:
                return render(request,'teacher/search_teacher.html', {'srct':match})

            else:
                return HttpResponse('Result Not Found')
        else:
            return HttpResponseRedirect('/app/searchteacher/')

    return render(request,'teacher/search_teacher.html')



def view_subject_lists(request):
    list_of_subject= Subject.objects.all()

    context_variable = {
        'subject':list_of_subject
    }

    return render(request,'subject/subject_list.html',context_variable)


def view_subject_list_page(request):
    return render(request,'subject/subject_list.html')

def view_subject_form(request):
    return render(request,'subject/subject_form.html')

def view_subjectdata_save(request):
    if request.method == "POST":
        get_all = request.POST
        get_code = request.POST['code']
        get_name = request.POST['name']
        get_class_name = request.POST['class_name']
        subject= Subject(code=get_code,name=get_name,class_name=get_class_name)
        subject.save()
        return redirect('/app/subjectlist/')
    else:
        return HttpResponse("Error record saving")


def view_subjectdata_updateform(request,ID):
    subject = Subject.objects.get(id=ID)
    context_varible = {
        'subjects': subject
    }
    return render(request,'subject/update_subject.html',context_varible)

def view_subject_update_form_data_in_db(request,ID):
    subject = Subject.objects.get(id=ID)
    list_of_subject = request.POST
    subject.code = request.POST['code']
    subject.name= request.POST['name']
    subject.class_name = request.POST['class_name']
    subject.save()
    return redirect('/app/subjectlist/')

def deletesubject(request, ID):
    subject = Subject.objects.get(id=ID)
    subject.delete()
    return redirect('/app/subjectlist/')

def searchsubject(request):
    if request.method=='POST':
        srch = request.POST['search']

        if srch:
            match = Subject.objects.filter(
                Q(code__icontains=srch) 
                )

            if match:
                return render(request,'subject/search_subject.html', {'searchsubject':match})

            else:
                return HttpResponse('Result Not Found')
        else:
            return HttpResponseRedirect('/app/searchsubject/')

    return render(request,'subject/search_subject.html')




def view_class_lists(request):
    list_of_class= Class.objects.all()

    context_variable = {
        'class':list_of_class
    }

    return render(request,'class/class_list.html',context_variable)


def view_class_list_page(request):
    return render(request,'class/class_list.htmll')

def view_class_form(request):
    return render(request,'class/class_form.html')

def view_class_data_save(request):
    if request.method == "POST":
        get_all = request.POST
        get_code = request.POST['code']
        get_class_name = request.POST['class_name']
        get_class_type = request.POST['class_type']
        class_obj= Class(code=get_code,class_name=get_class_name,class_type=get_class_type)
        class_obj.save()
        return redirect('/app/classlist/')
    else:
        return HttpResponse("Error record saving")


def view_class_updateform(request,ID):
    class_obj = Class.objects.get(id=ID)
    context_varible = {
        'classes': class_obj
    }
    return render(request,'class/update_class.html',context_varible)

def view_class_update_form_data_in_db(request,ID):
    class_obj = Class.objects.get(id=ID)
    list_of_class= request.POST
    class_obj.code = request.POST['code']
    class_obj.class_name= request.POST['class_name']
    class_obj.class_type = request.POST['class_type']
    class_obj.save()
    return redirect('/app/classlist/')

def deletetclass(request, ID):
    class_obj = Class.objects.get(id=ID)
    class_obj.delete()
    return redirect('/app/classlist/')

def searchclass(request):
    if request.method=='POST':
        srch = request.POST['search']

        if srch:
            match = Class.objects.filter(
                Q(code__icontains=srch) | Q(class_name__icontains=srch)
                )

            if match:
                return render(request,'class/search_class.html', {'searchclass':match})

            else:
                return HttpResponse('Result Not Found')
        else:
            return HttpResponseRedirect('/app/searchclass')

    return render(request,'class/search_class.html')

def view_parent_lists(request):
    list_of_parent= Parents.objects.all()

    context_variable = {
        'parent': list_of_parent    
    }

    return render(request,'parent/parent_list.html',context_variable)


def view_parent_list_page(request):
    return render(request,'parent/parent_list.html')

def view_parent_form(request):
    return render(request,'parent/parent_form.html')

def view_parent_data_save(request):
    if request.method == "POST":
        get_all = request.POST
        get_first_name = request.POST['first_name']
        get_last_name = request.POST['last_name']
        get_phone_no = request.POST['phone_no']
        get_address = request.POST['address']
        parent_obj = Parents(first_name=get_first_name,last_name=get_last_name,phone_no=get_phone_no,address=get_address)
        parent_obj.save()
        return redirect('/app/parentlist/')
    else:
        return HttpResponse("Error record saving")


def view_parent_updateform(request,ID):
    parent_obj = Parents.objects.get(id=ID)
    context_varible = {
        'parents': parent_obj
    }
    return render(request,'parent/update_parent.html',context_varible)

def view_parent_update_form_data_in_db(request,ID):
    parent_obj = Parents.objects.get(id=ID)
    parent_form_data = request.POST
    parent_obj.first_name = request.POST['first_name']
    parent_obj.last_name = request.POST['last_name']
    parent_obj.phone_no = request.POST['phone_no']
    parent_obj.address = request.POST['address']
    parent_obj.save()
    return redirect('/app/parentlist/')

def deleteparent(request, ID):
    parent_obj = Parents.objects.get(id=ID)
    parent_obj.delete()
    return redirect('/app/parentlist/')


def parentsearch(request):
    if request.method=='POST':
        srch = request.POST['search']

        if srch:
            match = Parents.objects.filter(
                Q(first_name__icontains=srch) | Q(address__icontains=srch)
                )

            if match:
                return render(request,'parent/search_parent.html', {'searchparent':match})

            else:
                return HttpResponse('Result Not Found')
        else:
            return HttpResponseRedirect('/app/searchparent/')

    return render(request,'parent/search_parent.html')



def view_result_lists(request):
    list_of_result= Result.objects.all()

    context_variable = {
        'result': list_of_result   
    }

    return render(request,'result/result_list.html',context_variable)


def view_result_list_page(request):
    return render(request,'result/result_list.html')

def view_result_form(request):
    return render(request,'result/result_form.html')

def view_result_data_save(request):
    if request.method == "POST":
        get_all = request.POST
        get_student_id = request.POST['student_id']
        get_student_name = request.POST['student_name']
        get_subject_code = request.POST['subject_code']
        get_subject_name = request.POST['subject_name']
        get_teacher_name = request.POST['teacher_name']
        get_marks_obtained = request.POST['marks_obtained']
        result_obj = Result(student_id=get_student_id,student_name=get_student_name,subject_code=get_subject_code,subject_name=get_subject_name,teacher_name=get_teacher_name,marks_obtained=get_marks_obtained)
        result_obj.save()
        return redirect('/app/resultlist/')
    else:
        return HttpResponse("Error record saving")


def view_result_updateform(request,ID):
    result_obj = Result.objects.get(id=ID)
    context_varible = {
        'results': result_obj
    }
    return render(request,'result/update_result.html',context_varible)

def view_result_update_form_data_in_db(request,ID):
    result_obj = Result.objects.get(id=ID)
    result_form_data = request.POST
    result_obj.student_id = request.POST['student_id']
    result_obj.student_name = request.POST['student_name']
    result_obj.subject_code = request.POST['subject_code']
    result_obj.subject_name = request.POST['subject_name']
    result_obj.teacher_name = request.POST['teacher_name']
    result_obj.marks_obtained = request.POST['marks_obtained']

    result_obj.save()
    return redirect('/app/resultlist/')

def deleteresult(request, ID):
    result_obj = Result.objects.get(id=ID)
    result_obj.delete()
    return redirect('/app/resultlist/')


def resultsearch(request):
    if request.method=='POST':
        srch = request.POST['search']

        if srch:
            match = Result.objects.filter(
                Q(student_id__icontains=srch) | Q(student_name__icontains=srch)
                )

            if match:
                return render(request,'result/search_result.html', {'srchres':match})

            else:
                return HttpResponse('Result Not Found')
        else:
            return HttpResponseRedirect('/app/searchresult/')

    return render(request,'result/search_result.html')