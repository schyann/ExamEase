from django.shortcuts import render,redirect,get_object_or_404 
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate, logout 
from django.http import JsonResponse 
# from django.contrib.auth.decorators import login_required
from django.http import HttpResponse  
from APP.create_test_sheets import create_sheet
from APP.forms import AnswerForm, StudentForm,uploadAnswerSheetForm  
from .models import Student,ExaminationMain,ExaminationDetails,answerKey,examResult
from APP.scanStart import scanSheet
from django.core import serializers
import datetime
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile


# Create your views here.

def signout_view(request):
    # logout(request)
    return redirect('/') 

def uploadAnswer(request):
    return render(request,'admin/uploadAnswerSheet.html')

def scan_paper(request):
     if request.method =="POST":
        image = request.POST['image']
        data = scanSheet(image)
        return JsonResponse(data, safe=False)

    #return render(request,'admin/dashboard.html',{'app_url': 'dashboard'})

def home(request):
    return render(request,'home.html')

def signup(request):
    return render(request,'registration/register.html')

def createPaper(request,Id):
    if request.method =='GET':        
        records = ExaminationDetails.objects.filter(ExaminationMain=Id).values()
        # data = serializers.serialize('json', records)
        data = list(records)
        create_sheet(data)
        return JsonResponse(data, safe=False)
    
def signin(request):
    return render(request,'registration/login.html')

# @login_required(login_url='/custom-login/')
def validate_username(request):
    """Check username availability"""
    username = request.GET.get('username', None)
    response = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(response)

# @login_required(login_url='/custom-login/')
def register(request):
    if request.method =="POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.create_user(first_name=firstname,last_name=lastname,username=username,password=password)
            user.save()
            # login(request,user)
            response = {
                'isSave': True,
                'message':"success"
            }
            return JsonResponse(response)
        except Exception as e:
            response = {
                'isSave': False,
            }
            return JsonResponse(response)

# @login_required(login_url='signin')
def logIn(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        #current_user = request.user
        if user is not None:
            login(request,user)
            response = {
                'isSave': True,
                'message':"success",
                'userId': user.id,
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
            }
            return JsonResponse(response)
        else:
            response = {
                'isSave': False,
            }
            return JsonResponse(response)

# def dashboard(request):
#     return render(request,'admin/dashboard.html',{'app_url': 'dashboard'})

def answerKeyMain(request): 
    if request.user.is_authenticated: 
        records = ExaminationMain.objects.filter(user_id=request.user.id)
        context = {
            'app_url': 'answerkey', 
            'records': records,
        }
    return render(request,'admin/answerKey.html',context) 
    # return render(request,'admin/examination.html',{'app_url': 'examination'})
  
def student(request):
    if request.user.is_authenticated: 
        records = Student.objects.filter(user_id=request.user.id)
        context = {
            'app_url': 'student', 
            'records': records,
        }
    return render(request,'admin/student.html',context) 

def saveStudent(request):    
    if request.method =="POST":
        try:
            student = Student(StudentId=request.POST['StudentId'],Firstname=request.POST['Firstname'], Lastname=request.POST['Lastname'], Middlename=request.POST['Middlename'],user_id=request.user.id)
            student.save() 
            # login(request,user)
            response = {
                'isSave': True,
                'message':"success"
            }
            return JsonResponse(response)
        except Exception as e:
            response = {
                'isSave': False,
            }
            print(f"An unexpected error occurred: {e}")
            return JsonResponse(response)
 
def getStudent(request, Id):
    if request.method == 'GET':
        record = get_object_or_404(Student, Id=Id)
        data = {
            'Id': record.Id, 
            'StudentId': record.StudentId, 
            'Firstname': record.Firstname, 
            'Lastname': record.Lastname, 
            'Middlename': record.Middlename, 
            # Add other fields as needed
        }
        return JsonResponse(data)

    # student = Student.objects.get(Id=Id)
    # response = {'student': student}
    # return JsonResponse(response)

def updateStudent(request, Id): 
    if request.method =="POST":
        try: 
            student = Student.objects.get(Id=Id)  
           # form = Student(StudentId=request.POST['StudentId'],Firstname=request.POST['Firstname'], Lastname=request.POST['Lastname'], Middlename=request.POST['Middlename'],user_id=request.user.id)
            
            form = StudentForm(request.POST, instance = student) 
            form.save()
            response = {
                'isSave': True,
                'message':"success"
            }
            return JsonResponse(response)
        except Exception as e:
            response = {
                'isSave': False,
            }
            print(f"An unexpected error occurred: {e}")
            return JsonResponse(response)
        
    # return render(request, 'edit.html', {'employee': employee}) 

def updateAnswer(request, Id): 
    if request.method =="POST":
        try: 
            ans = answerKey.objects.get(Id=Id)  
           # form = Student(StudentId=request.POST['StudentId'],Firstname=request.POST['Firstname'], Lastname=request.POST['Lastname'], Middlename=request.POST['Middlename'],user_id=request.user.id)
            
            form = AnswerForm(request.POST, instance = ans) 
            form.save()
            response = {
                'isSave': True,
                'message':"success"
            }
            return JsonResponse(response)
        except Exception as e:
            response = {
                'isSave': False,
            }
            print(f"An unexpected error occurred: {e}")
            return JsonResponse(response)
        
    # return render(request, 'edit.html', {'employee': employee}) 


def deleteAnswer(request, Id): 
    try: 
        ans = answerKey.objects.get(Id=Id)  
        ans.delete()   
        response = {
            'isSave': True,
            'message':"success"
        }
        return JsonResponse(response)
    except Exception as e:
        response = {
            'isSave': False,
        }
        print(f"An unexpected error occurred: {e}")
        return JsonResponse(response)
    

def deleteStudent(request, Id): 
    try: 
        employee = Student.objects.get(Id=Id)  
        employee.delete()   
        response = {
            'isSave': True,
            'message':"success"
        }
        return JsonResponse(response)
    except Exception as e:
        response = {
            'isSave': False,
        }
        print(f"An unexpected error occurred: {e}")
        return JsonResponse(response)
    
def deleteExam(request, Id): 
    try: 
        examMain = ExaminationMain.objects.get(Id=Id)  
        examMain.delete()   
        response = {
            'isSave': True,
            'message':"success"
        }
        return JsonResponse(response)
    except Exception as e:
        response = {
            'isSave': False,
        }
        print(f"An unexpected error occurred: {e}")
        return JsonResponse(response)
   
def dashboard(request):
    if request.user.is_authenticated: 
        studentCount = Student.objects.filter(user_id=request.user.id).count()
        ExamCount = ExaminationMain.objects.filter(user_id=request.user.id).count() 
        print(studentCount)
        print(ExamCount) 
        context = {
            'app_url': 'examination', 
            'sCount': studentCount,
            'eCount': ExamCount,
        }
    return render(request,'admin/dashboard.html',context) 

def deleteStudentExam(request, StudentId,Id): 
    
    if request.user.is_authenticated: 
        try:  
            print(StudentId)
            print(Id)
            examinationDetails = ExaminationDetails.objects.get(ExaminationMain=StudentId,StudentIdNo=Id)  
            examinationDetails.delete()   
            response = {
                'isSave': True,
                'message':"success"
            }
            return JsonResponse(response)
        except Exception as e:
            response = {
                'isSave': False,
            }
            print(f"An unexpected error occurred: {e}")
            return JsonResponse(response)

def examinationMain(request): 
    if request.user.is_authenticated: 
        records = ExaminationMain.objects.filter(user_id=request.user.id)
        context = {
            'app_url': 'examination', 
            'records': records,
        }
    return render(request,'admin/Examination.html',context) 
    # return render(request,'admin/examination.html',{'app_url': 'examination'})

def examinationDetail(request,Id):
    if request.user.is_authenticated: 
        records = ExaminationDetails.objects.filter(ExaminationMain=Id).values_list('StudentIdNo', flat=True)
        studentsExam = Student.objects.filter(StudentId__in=records)
        excludedstudents = Student.objects.exclude(StudentId__in=records)

        studentsExamdata = list(studentsExam)           
        excludedstudentsdata = list(excludedstudents)  
        context = {
            'app_url': 'examination', 
            'studentsExam': studentsExamdata,
            'excludedstudents': excludedstudentsdata,
        }
    return render(request,'admin/examinationDetail.html',context) 
    # return render(request,'admin/examinationDetail.html',{'app_url': 'dashboard'})

def getExaminee(request, Id):
    if request.method =='GET':
        records = ExaminationDetails.objects.filter(ExaminationMain=Id).values() 
        # data = serializers.serialize('json', records)
        data = list(records)
        
        return JsonResponse(data, safe=False)
        #return render(request,'admin/examination.html',context) 
    # return render(request,'admin/examinationDetail.html',{'app_url': 'dashboard'})

def saveExaminee(request):
     if request.method =="POST":
        try:
            examinationDetails = ExaminationDetails(Student_id=request.POST['Student_Id'],ExaminationMain=request.POST['ExaminationMain_id'], StudentIdNo=request.POST['StudentIdNo'], Fullname=request.POST['Fullname'],user_id=request.user.id)
            examinationDetails.save()   
            # login(request,user)
            response = {
                'isSave': True,
                'message':"success"
            }
            return JsonResponse(response)
        except Exception as e:
            response = {
                'isSave': False,
            }
            print(f"An unexpected error occurred: {e}")
            return JsonResponse(response)

def examination(request):
    if request.user.is_authenticated: 
        records = ExaminationMain.objects.filter(user_id=request.user.id)
        context = {
            'app_url': 'examination', 
            'records': records,
        }

        return render(request,'admin/Examination.html',context) 

def examinationMain(request):
     
     if request.method =="POST":
        try:
            examinationMain = ExaminationMain(ExaminationId=request.POST['ExaminationId'],user_id=request.user.id)
            examinationMain.save() 
            # login(request,user)
            response = {
                'isSave': True,
                'message':"success"
            }
            return JsonResponse(response)
        except Exception as e:
            response = {
                'isSave': False,
            }
            print(f"An unexpected error occurred: {e}")
            return JsonResponse(response)
        
def saveAnsKey(request):
    if request.method =="POST":
        try:
            ans = answerKey(ExaminationId=request.POST['Examinationid'], Item=request.POST['ItemNo'],Answer=request.POST['Answer'],user_id=request.user.id)
            ans.save()   
            # login(request,user)
            response = {
                'isSave': True,
                'message':"success",
                'Id': ans.Id,
                'Item':ans.Item,
                'Answer':ans.Answer
            }
            return JsonResponse(response)
        except Exception as e:
            response = {
                'isSave': False,
            }
            print(f"An unexpected error occurred: {e}")
            return JsonResponse(response)

def getanswerKey(request, Id):
    if request.method =='GET':
        records = answerKey.objects.filter(ExaminationId=Id).values()
        # data = serializers.serialize('json', records)
        data = list(records)
        context = {
            'app_url': 'examination', 
            'datas': records,
        }
        return JsonResponse(data, safe=False)
        #return render(request,'admin/examination.html',context) 
    # return render(request,'admin/examinationDetail.html',{'app_url': 'dashboard'})

# def upload_image(request):
#     if request.method == 'POST' and request.FILES.get('image'):
#         form = uploadAnswerSheetForm(request.POST, request.FILES)
#         if form.is_valid():
#             image_instance = form.save()
#             uploaded_file = request.FILES['image']  # 'file' is the name of the input field
#             file_name = uploaded_file.name  # Gets the name of the uploaded file
#             # Return the URL of the uploaded image as a JSON response
#             # image_url = str("media/uploads").image.url
#             return JsonResponse({'success': True,"file_name":file_name})
#         else:
#             return JsonResponse({'success': False, 'error': 'Invalid form data'})
#     return JsonResponse({'success': False, 'error': 'No file uploaded'})


def upload_image(request):
    if request.method == 'POST' and request.FILES:
        uploaded_file = request.FILES['image']
        # Get the file extension
        ext = uploaded_file.name.split('.')[-1]
        # Create a new filename
        # new_filename = f"{uuid.uuid4()}.{ext}"

        # Generate timestamp
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        # Use the timestamp in a filename
        filename = f"{timestamp}.{ext}"
        # Save the file with the new name
        file_path = default_storage.save(f'uploads/{filename}', ContentFile(uploaded_file.read()))
        return JsonResponse({'success': True,"file_name":filename}) 
    return JsonResponse({'success': False, 'error': 'No file uploaded'})


def saveResult(request):
    if request.method =="POST":
        try:
            examresult = examResult(ExaminationId=request.POST['ExaminationId'], StudentIdNo=request.POST['StudentIdNo'],Fullname=request.POST['Fullname'],Items=request.POST['Items'],Score=request.POST['Score'],user_id=request.user.id)
            examresult.save()   
            # login(request,user)
            response = {
                'isSave': True,
                'message':"success"
            }
            return JsonResponse(response)
        except Exception as e:
            response = {
                'isSave': False,
            }
            print(f"An unexpected error occurred: {e}")
            return JsonResponse(response)
 
def examinationResult(request):
    if request.user.is_authenticated: 
        records = ExaminationMain.objects.filter(user_id=request.user.id)
        context = {
            'app_url': 'examinationResult', 
            'records': records,
        }
    return render(request,'admin/examResult.html',context) 

def examResultDetails(request,Id):
    if request.method =='GET':
        records = examResult.objects.filter(ExaminationId=Id).values('StudentIdNo','Fullname','Items','Score').distinct()
        # data = serializers.serialize('json', records)
        data = list(records)
        context = {
            'app_url': 'examinationResult', 
            'datas': records,
        }
        return JsonResponse(data, safe=False)
        #return render(request,'admin/examination.html',context) 
    # return render(request,'admin/examinationDetail.html',{'app_url': 'dashboard'})







