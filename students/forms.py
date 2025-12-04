from django import forms

from .models import Course, Registration, Student


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
        # Adicione isso para ficar bonito no HTML
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(
                attrs={'class': 'form-control', }), }


class RegisterCourse(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'workload', 'registration_fee', 'is_active']
