from django.urls import path

from . import views

urlpatterns = [
    path("", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("logout/", views.logout_view, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("students/", views.students, name="students"),
    path("courses", views.courses, name="courses"),
    path(
        'students/edit/<int:id>/', views.student_edit, name="student_edit"),
    path(
        'students/delete/<int:id>/', views.student_delete,
        name="student_delete"),
    path("courses/edit/<int:id>/", views.course_edit, name="course_edit"),
    path("courses/delete/<int:id>/", views.course_delete, name="course_delete")
]
