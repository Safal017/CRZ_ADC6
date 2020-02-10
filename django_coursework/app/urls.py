from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('home/',view_home_page),
    path('test/',view_students_list_page),
    path('studentlist/',view_students_lists),
    path('studentform/',view_student_form),
    path('studentform/save',view_studentdata_save),
    path('studentlist/edit/<int:ID>',view_Studentdata_updateform),
    path('studentlist/edit/update/<int:ID>',view_student_update_form_data_in_db),
    path('teacherform/',view_teacher_form),
    path('teacherlist/',view_teacher_lists),
    path('teacherform/save',view_teacherdata_save),
    path('teacherlist/edit/<int:ID>',view_teacherdata_updateform),
    path('teacherlist/edit/update/<int:ID>',view_teacher_update_form_data_in_db),
    path('subjectlist/',view_subject_lists),
    path('subjectform/',view_subject_form),
    path('subjectform/save',view_subjectdata_save),
    path('subjectlist/edit/<int:ID>',view_subjectdata_updateform),
    path('subjectlist/edit/update/<int:ID>',view_subject_update_form_data_in_db),
    path('classlist/',view_class_lists),
    path('classform/',view_class_form),
    path('classform/save',view_class_data_save),
    path('classlist/edit/<int:ID>',view_class_updateform),
    path('classlist/edit/update/<int:ID>',view_class_update_form_data_in_db),
    path('parentlist/',view_parent_lists),
    path('parentform/',view_parent_form),
    path('parentform/save',view_parent_data_save),
    path('parentlist/edit/<int:ID>',view_parent_updateform),
    path('parentlist/edit/update/<int:ID>',view_parent_update_form_data_in_db),
    path('resultlist/',view_result_lists),
    path('resultform/',view_result_form),
    path('resultform/save',view_result_data_save),
    path('resultlist/edit/<int:ID>',view_result_updateform),
    path('resultlist/edit/update/<int:ID>',view_result_update_form_data_in_db),
   
]