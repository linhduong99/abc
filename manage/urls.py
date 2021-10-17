from django.urls import path
from .views import ListCreateStudentView, GetStudentView

urlpatterns = [
    path('students', ListCreateStudentView.as_view(), name='create_student'),
    path('students/<int:id>', GetStudentView.as_view(), name='getUser')

]
