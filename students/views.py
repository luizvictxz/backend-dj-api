from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import RegistrationStudentForm
from .models import Course, Registration, Student

# Create your views here.


def login(request):
    return render(request, "login.html")


def dashboard(request):
    students_all = Student.objects.count()
    courses_is_active = Course.objects.filter(is_active=True).count()
    value = Registration.objects.filter(
        status="PAGO")

    sum = 0
    for i in value:
        sum += i.course.registration_fee

    registration_lasts = Registration.objects.select_related(
        "student", "course").order_by('-id')[:5]

    print(registration_lasts)

    context = {
        'total_alunos': students_all,
        'cursos_ativos': courses_is_active,
        'receita_total': sum,
        'matriculas': registration_lasts,
        'active': 'dash'
    }
    return render(request, "dashboard.html", context)


def students(request):
    if request.method == "POST":
        form = RegistrationStudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Matrícula realizada com sucesso!')
            return redirect('students')
        messages.error(request, 'Erro ao salvar. Verifique os campos abaixo.')
    else:
        form = RegistrationStudentForm()
    students_all = Registration.objects.select_related(
        "student", "course").order_by("-id")
    context = {
        'active': 'stu',
        'matriculas': students_all,
        'form': form
    }
    return render(request, "students.html", context)


def courses(request):
    courses_all = Course.objects.all().order_by('-id')
    context = {
        'active': 'cour',
        'cursos': courses_all
    }
    return render(request, "courses.html", context)
