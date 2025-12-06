from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Sum
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DeleteView, UpdateView

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


class DashboardView(LoginRequiredMixin, View):
    template_name = "dashboard.html"

    def get(self, request):
        number_students = Student.objects.count()
        courses_actives = Course.objects.filter(is_active=True).count()

        receive = Registration.objects.filter(status="PAGO").aggregate(
            value=Sum('course__registration_fee')
        )['value']

        receive_all = receive if receive else 0

        last_regis = Registration.objects.select_related(
            'student', 'course').order_by('-id')[:5]

        context = {
            'total_alunos': number_students,
            'cursos_ativos': courses_actives,
            'receita_total': receive_all,
            'matriculas': last_regis,
            'active': 'dash'
        }
        return render(request, self.template_name, context)


class StudentView(LoginRequiredMixin, View):
    form_regis_class = RegistrationStudentForm
    form_stu_class = RegisterStudent
    template_name = "students.html"

    def get(self, request):
        context = {
            'active': 'stu',
            'alunos': Student.objects.prefetch_related(
                "registration_set__course").order_by("-id"),
            'form_regis': self.form_regis_class(),
            'form_stu': self.form_stu_class()
        }
        return render(
            request, self.template_name,
            context)

    def post(self, request):
        form_stu = self.form_stu_class()
        form_regis = self.form_regis_class()

        if 'btn-mat' in request.POST:
            form_regis = self.form_regis_class(request.POST)
            if form_regis.is_valid():
                form_regis.save()
                messages.success(request, 'Matrícula realizada com sucesso!')
                return redirect('students')
        elif 'btn-al' in request.POST:
            form_stu = self.form_stu_class(request.POST)
            if form_stu.is_valid():
                form_stu.save()
                messages.success(request, 'Aluno cadastrado com sucesso!')
                return redirect('students')

        messages.error(request, 'Erro ao salvar. Verifique os campos.')
        return redirect("students")


class StudentUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Student
    form_class = RegisterStudent
    success_url = reverse_lazy("students")

    success_message = "Aluno atualizado com sucesso!"


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    success_url = reverse_lazy("students")

    def form_valid(self, form):
        messages.success(self.request, "Aluno excluído com sucesso!")
        return super().form_valid(form)


class CourseView(LoginRequiredMixin, View):
    form_class = RegisterCourse
    template_name = "courses.html"

    def get(self, request):
        context = {
            'active': 'cour',
            'cursos': Course.objects.all().order_by('-id'),
            'form': self.form_class()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Curso adicionado com sucesso!")
            return redirect("courses")


class CourseUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Course
    form_class = RegisterCourse
    success_url = reverse_lazy("courses")
    success_message = "Curso atualizado com sucesso!"


class CourseDeleteView(LoginRequiredMixin, UpdateView):
    model = Course
    success_url = reverse_lazy("courses")

    def form_valid(self, form):
        messages.success(self.request, "Aluno excluído com sucesso!")
        return super().form_valid(form)


class FinancciView(LoginRequiredMixin, View):
    def get(self, request):
        students = Student.objects.prefetch_related("registration_set__course")
        financci_data = []

        all_school = 0
        miss_school = 0
        # Falta terminar
        for student in students:
            paid_student = 0
            miss_student = 0

            for reg in student.registration_set.all():
                valor = reg.course.registration_fee
                if reg.status == "PAGO":
                    paid_student += valor
                else:
                    miss_student += valor

            all_school += paid_student
            miss_school += miss_student

            if paid_student > 0 or miss_student > 0:
                financci_data.append({
                    'aluno': student,
                    'pago': paid_student,
                    'pendente': miss_student,
                    'total_geral': paid_student + miss_student,

                })

        context = {
            'active': 'fina',
            'dados': financci_data,
            'receita_total': all_school,
            'pendente_total': miss_school
        }
        return render(request, "financci.html", context)
