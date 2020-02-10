from django.urls import path
from .views import *

urlpatterns = [
    path('teachers/',view_get_post_teacher),
    path('teachers/<int:ID>',view_put_delete_teacher),
    path('subjects/',view_get_post_subject),
    path('students/',view_get_post_student),
    path('classes/',view_get_post_class),
    path('parents/',view_get_post_parents),
    path('students/',view_get_post_student),
    path('parents/<int:ID>',view_parents_getByID_updateByID_deleteByID),
    path('students/<int:PAGENO>', api_student_pagination),
    
]