from django.urls import path
from .views import *
urlpatterns = [
path('teachers/<int:ID>',view_put_delete_teacher),
 path('students/<int:PAGENO>', api_student_pagination),
    
]