from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    date_into = models.DateField(auto_created=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=200)
    workload = models.IntegerField()
    registration_fee = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Registration(models.Model):
    class StatusChoice(models.TextChoices):
        PENDING = 'PENDENTE', 'Pendente'
        PAID = 'PAGO', 'Pago'

    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=10, choices=StatusChoice.choices,
        default=StatusChoice.PENDING)

    class Meta:
        unique_together = ('student', 'course')

    def __str__(self):
        return f"{self.student.name} - {self.course.name}"
