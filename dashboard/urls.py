from django.urls import path
from .views import *
urlpatterns = [
    path('university/', UniversityListCreateApiView.as_view()),
    path('university/<int:pk>', UniversityRetrieveUpdateDestroyAPIView.as_view()),
    path('faculty/', FacultyListCreateApiView.as_view()),
    path('faculty/<int:pk>', FacultyRetrieveUpdateDestroyAPIView.as_view()),
    path('group/<int:pk>', GroupRetrieveUpdateDestroyAPIView.as_view()),
    path('teacher/', TeacherListCreateApiView.as_view()),
    path('teacher/<int:pk>', TeacherRetrieveUpdateDestroyAPIView.as_view()),
    path('subject/', SubjectListCreateApiView.as_view()),
    path('subject/<int:pk>', SubjectRetrieveUpdateDestroyAPIView.as_view()),
    path('student/', StudentListCreateApiView.as_view()),
    path('student/<int:pk>', StudentRetrieveUpdateDestroyAPIView.as_view()),
]
