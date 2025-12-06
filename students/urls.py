from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import api_views, views
from .views import (
    CourseDeleteView,
    CourseUpdateView,
    CourseView,
    DashboardView,
    FinancciView,
    StudentDeleteView,
    StudentUpdateView,
    StudentView,
)

router = DefaultRouter()
router.register(r'students', api_views.StudentViewSet)
router.register(r'courses', api_views.CourseViewSet)
router.register(r'registrations', api_views.RegistrationViewSet)


urlpatterns = [
    path("", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("logout/", views.logout_view, name="logout"),
    path("dashboard/", DashboardView.as_view(),
         name="dashboard"),
    path("students/", StudentView.as_view(),
         name="students"),
    path("courses/", CourseView.as_view(),
         name="courses"),
    path(
        'students/edit/<int:pk>/', StudentUpdateView.as_view(),
        name="student_edit"),
    path(
        'students/delete/<int:pk>/', StudentDeleteView.as_view(),
        name="student_delete"),
    path(
        "courses/edit/<int:pk>/", CourseUpdateView.as_view(),
        name="course_edit"),
    path(
        "courses/delete/<int:pk>/", CourseDeleteView.as_view(),
        name="course_delete"),
    path("financci/", FinancciView.as_view(),
         name="financci"),
    path('api/', include(router.urls)),
    path(
        'api/financial-report/', api_views.FinancialReportAPIView.as_view(),
        name="financial_report")]
