from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.db.models import Sum
from django.shortcuts import redirect, render

from .forms import RegistrationStudentForm
from .models import Course, Registration, Student


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("dashboard")
        messages.error(request, "Usuário ou senha inválidos.")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuário criado! Faça login.")
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


@login_required
def dashboard_view(request):
    # Contagens simples
    total_alunos = Student.objects.count()
    cursos_ativos = Course.objects.filter(is_active=True).count()

    receita = Registration.objects.filter(status="PAGO").aggregate(
        total=Sum('course__registration_fee')
    )['total']

    receita_total = receita if receita else 0

    # Listagem das últimas 5 matrículas
    ultimas_matriculas = Registration.objects.select_related(
        "student", "course").order_by('-id')[:5]

    context = {
        'total_alunos': total_alunos,
        'cursos_ativos': cursos_ativos,
        'receita_total': receita_total,
        'matriculas': ultimas_matriculas,
        'active': 'dash'
    }
    return render(request, "dashboard.html", context)

# --- MATRÍCULAS ---


@login_required
def students_view(request):
    if request.method == "POST":
        form = RegistrationStudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Matrícula realizada com sucesso!')
            return redirect('students')
        messages.error(request, 'Erro ao salvar. Verifique os campos.')
    else:
        form = RegistrationStudentForm()

    matriculas_all = Registration.objects.select_related(
        "student", "course").order_by("-id")

    context = {
        'active': 'stu',
        'matriculas': matriculas_all,
        'form': form
    }
    return render(request, "students.html", context)


@login_required
def courses_view(request):
    courses_all = Course.objects.all().order_by('-id')
    context = {
        'active': 'cour',
        'cursos': courses_all
    }
    return render(request, "courses.html", context)
