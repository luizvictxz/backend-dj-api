from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.db.models import Sum
from django.shortcuts import get_object_or_404, redirect, render

from .forms import RegisterCourse, RegisterStudent, RegistrationStudentForm
from .models import Course, Registration, Student


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("dashboard")
        print("ERROS DO FORM:", form.errors)
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
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard(request):
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


@login_required
def students(request):
    form_regis = RegistrationStudentForm()
    form_stu = RegisterStudent()
    if request.method == "POST":
        if 'btn-mat' in request.POST:

            form_regis = RegistrationStudentForm(request.POST)
            if form_regis.is_valid():
                form_regis.save()
                messages.success(request, 'Matrícula realizada com sucesso!')
                return redirect('students')
            messages.error(request, 'Erro ao salvar. Verifique os campos.')
        elif 'btn-al' in request.POST:
            form_stu = RegisterStudent(request.POST)
            if form_stu.is_valid():
                form_stu.save()
                messages.success(request, 'Aluno cadastrado com sucesso!')
                return redirect('students')
            messages.error(request, 'Erro ao salvar. Verifique os campos.')

    students_all = Student.objects.all().order_by("-id")

    context = {
        'active': 'stu',
        'alunos': students_all,
        'form_regis': form_regis,
        'form_stu': form_stu
    }
    return render(request, "students.html", context)


@login_required
def student_edit(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == "POST":
        form = RegisterStudent(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Aluno atualizado com sucesso!")
            return redirect('students')
    return redirect('students')


@login_required
def student_delete(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == "POST":
        student.delete()
        messages.success(request, "Aluno excluído com sucesso!")
    return redirect('students')


@login_required
def courses(request):
    courses_all = Course.objects.all().order_by('-id')
    if request.method == 'POST':
        form = RegisterCourse(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Curso adicionado com sucesso!")
            return redirect('courses')
    else:
        form = RegisterCourse()

    context = {
        'active': 'cour',
        'cursos': courses_all,
        'form': form
    }
    return render(request, "courses.html", context)
