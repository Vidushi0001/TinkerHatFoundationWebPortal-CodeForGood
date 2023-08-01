from django.contrib import admin
from django.urls import path
from home import views
from .views import StudentAPIView, StudentDetails, volunteerAPIView,volunteerDetails, ClassAPIView,ClassDetails, CoursesAPIView,CoursesDetails, question_answerAPIView, question_answerDetails, feedbackAPIView, feedbackDetails, testsAPIView, testsDetails, curriculumAPIView, curriculumDetails
urlpatterns = [
    path("register",views.register,name='register'),
    path("login",views.loginPage,name='login'),
    path("logoutUser",views.logoutUser,name='logoutUser'),

    path("student/api/",StudentAPIView.as_view()),
    path("student/api/<int:pk>/",StudentDetails.as_view()),

    path("volunteer/api/",volunteerAPIView.as_view()),
    path("volunteer/api/<int:pk>/",volunteerDetails.as_view()),

    path("class/api/",ClassAPIView.as_view()),
    path("class/api/<int:pk>/",ClassDetails.as_view()),

    path("courses/api/",CoursesAPIView.as_view()),
    path("courses/api/<int:pk>/",CoursesDetails.as_view()),

    path("question_answer/api/",question_answerAPIView.as_view()),
    path("question_answer/api/<int:pk>/",question_answerDetails.as_view()),

    path("feedback/api/",feedbackAPIView.as_view()),
    path("feedback/api/<int:pk>/",feedbackDetails.as_view()),

   path("tests/api/",testsAPIView.as_view()),
    path("tests/api/<int:pk>/",testsDetails.as_view()),

   path("curriculum/api/",curriculumAPIView.as_view()),
    path("curriculum/api/<int:pk>/",curriculumDetails.as_view()),

]


