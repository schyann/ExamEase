from django.urls import path
from . import views

urlpatterns=[   
    path("",views.home, name='home'),    
    path("signup",views.signup, name='signup'),
    path("signin",views.signin, name='signin'),
    path('signout', views.signout_view, name='signout'),
    path('validate_username', views.validate_username, name='validate_username'),
    path("register",views.register, name='register'),
    path("logIn",views.logIn, name='logIn'),
    path("dashboard",views.dashboard, name='dashboard'),

    path("student",views.student, name='student'),
    path("saveStudent",views.saveStudent, name='saveStudent'),  
    path('getStudent/<int:Id>/', views.getStudent, name='getStudent'),
    path('updateStudent/<int:Id>/', views.updateStudent, name='updateStudent'),
    path('updateAnswer/<int:Id>/', views.updateAnswer, name='updateAnswer'),
    path('deleteStudent/<int:Id>/', views.deleteStudent, name='deleteStudent'), 
    path('deleteAnswer/<int:Id>/', views.deleteAnswer, name='deleteAnswer'), 
    
    path("examination",views.examination, name='examination'),
    path("examinationMain",views.examinationMain, name='examinationMain'), 
    path("examinationDetail/<int:Id>/",views.examinationDetail, name='examinationDetail'), 
    path('deleteStudentExam/<str:Id>/<int:StudentId>/', views.deleteStudentExam, name='deleteStudentExam'),
    path("deleteExam/<int:Id>/",views.deleteExam, name='deleteExam'),  
    
    path("saveExaminee",views.saveExaminee, name='saveExaminee'), 
    path("getExaminee/<int:Id>/",views.getExaminee, name='getExaminee'), 
    path("scan_paper",views.scan_paper, name='scan_paper'),

    path("uploadAnswer",views.uploadAnswer, name='uploadAnswer'),
    path("answerKeyMain",views.answerKeyMain, name='answerKeyMain'),
    path("saveAnsKey",views.saveAnsKey, name='saveAnsKey'),  
    path("getanswerKey/<int:Id>/",views.getanswerKey, name='getanswerKey'), 
    path('upload/', views.upload_image, name='upload_image'), 
    path("saveResult",views.saveResult, name='saveResult'),

    path("examinationResult",views.examinationResult, name='examinationResult'),
    path("examResultDetails/<int:Id>/",views.examResultDetails, name='examResultDetails'), 
    
    path("createPaper/<int:Id>/",views.createPaper, name='createPaper'), 
    

]