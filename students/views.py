from django.db.models import Sum
from django.shortcuts import render

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
        'matriculas': registration_lasts
    }
    return render(request, "dashboard.html", context)


def students(request):
    return render(request, "students.html")


def courses(request):
    return render(request, "courses.html")
