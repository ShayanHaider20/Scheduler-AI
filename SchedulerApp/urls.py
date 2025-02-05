from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    
    ##NEW LINE
    path('static/CSS/style.css', my_css_view, name='my_css'),
    path('static/CSS/login.css', my_login_view, name='my_css'),
    path('static/js/script.js', my_js_view, name='my_js'),
    path('static/img/logo.jpg', my_img_view, name='my_img'),
    path('accounts/logout/',userlogout ,name = 'logout'),
    ##################################  GPT
     #path('accounts/login/', login_view, name='login'),
    path('generate_timetable/', generate_timetable, name='generate_timetable'),

    ##
    path('timetableGeneration/', timetable, name='timetable'),

    path('instructorAdd/', instructorAdd, name='instructorAdd'),
    path('instructorEdit/', instructorEdit, name='instructorEdit'),
    path('instructorDelete/<int:pk>/', instructorDelete, name='deleteinstructor'),

    path('roomAdd/', roomAdd, name='roomAdd'),
    path('roomEdit/', roomEdit, name='roomEdit'),
    path('roomDelete/<int:pk>/', roomDelete, name='deleteroom'),

    path('meetingTimeAdd/', meetingTimeAdd, name='meetingTimeAdd'),
    path('meetingTimeEdit/', meetingTimeEdit, name='meetingTimeEdit'),
    path('meetingTimeDelete/<str:pk>/', meetingTimeDelete, name='deletemeetingtime'),

    path('courseAdd/', courseAdd, name='courseAdd'),
    path('courseEdit/', courseEdit, name='courseEdit'),
    path('courseDelete/<str:pk>/', courseDelete, name='deletecourse'),

    path('departmentAdd/', departmentAdd, name='departmentAdd'),
    path('departmentEdit/', departmentEdit, name='departmentEdit'),
    path('departmentDelete/<int:pk>/', departmentDelete, name='deletedepartment'),

    path('sectionAdd/', sectionAdd, name='sectionAdd'),
    path('sectionEdit/', sectionEdit, name='sectionEdit'),
    path('sectionDelete/<str:pk>/', sectionDelete, name='deletesection'),

    path('api/genNum/', apiGenNum, name='apiGenNum'),
    path('api/terminateGens/', apiterminateGens, name='apiterminateGens')
]
