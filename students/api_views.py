from django.db import connection
from django.db.models import Count, F, Q, Sum
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Course, Registration, Student
from .serializers import CourseSerializer, RegistrationSerializer, StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all().order_by("-id")

    @action(detail=True, methods=['get'])
    def registrations(self, request, pk=None):
        student = self.get_object()
        matriculas = Registration.objects.filter(student=student)
        serializer = RegistrationSerializer(matriculas, many=True)

        return Response(serializer.data)


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all().order_by("-id")

    @action(detail=False, methods=['get'])
    def statistics(self, request):

        query = """
            SELECT 
                c.name, 
                COUNT(r.id) as total
            FROM 
                students_course c
            LEFT JOIN 
                students_registration r ON c.id = r.course_id
            GROUP BY 
                c.name
            ORDER BY
                total DESC
        """

        with connection.cursor() as cursor:
            cursor.execute(query)
            rows = cursor.fetchall()

        data = []
        for row in rows:
            data.append({
                "curso": row[0],
                "alunos_matriculados": row[1]
            })

        return Response(data)


class RegistrationViewSet(viewsets.ModelViewSet):
    serializer_class = RegistrationSerializer
    queryset = Registration.objects.all().order_by("-id")

    def get_queryset(self):
        queryset = Registration.objects.all()
        student_id = self.request.query_params.get('student_id')
        if student_id:
            queryset = queryset.filter(student_id=student_id)
        return queryset

    @action(detail=True, methods=['post'])
    def mark_as_paid(self, request, pk=None):
        registration = self.get_object()
        registration.status = 'PAGO'
        registration.save()
        return Response(
            {'status': 'Matrícula marcada como paga'},
            status=status.HTTP_200_OK)


class FinancialReportAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        all_courses = Course.objects.annotate(total=Count("registration"))

        students_due = Student.objects.annotate(
            divida=Sum(
                F('registration__course__registration_fee'),
                filter=Q(registration__status='PENDENTE')
            )
        )

        total_due = Registration.objects.filter(
            status="PENDENTE").aggregate(
            total=Sum("course__registration_fee"))["total"]

        courses_data = []
        for course in all_courses:
            courses_data.append({
                "curso": course.name,
                "total_matriculas": course.total
            })

        students_data = []
        for student in students_due:
            valor_divida = student.divida if student.divida else 0

            students_data.append({
                "aluno": student.name,
                "total_devido": valor_divida
            })

        total_geral_valor = total_due if total_due else 0

        report_data = {
            "relatorio_cursos": courses_data,
            "relatorio_financeiro_alunos": students_data,
            "kpi_geral": {
                "total_pendente_escola": total_geral_valor
            }
        }

        return Response(report_data)
