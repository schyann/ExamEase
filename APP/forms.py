from django import forms  
from .models import Student, answerKey,uploadAnswerSheet 

class StudentForm(forms.ModelForm):  
    class Meta:  
        model = Student  
        fields = ['StudentId', 'Firstname', 'Lastname', 'Middlename'] 

class AnswerForm(forms.ModelForm):  
    class Meta:  
        model = answerKey  
        fields = ['Item', 'Answer'] 


class uploadAnswerSheetForm(forms.ModelForm):
    class Meta:
        model = uploadAnswerSheet
        fields = ['image']