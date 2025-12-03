from django import forms

from .models import Registration, Student


class RegistrationStudentForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['student', 'course']
        widgets = {
            'student': forms.Select(attrs={
                'class': 'form-select',
                'placeholder': 'Escolha o aluno'
            }),
            'course': forms.Select(attrs={
                'class': 'form-select'
            }),
        }


class RegisterStudent(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'cpf']
