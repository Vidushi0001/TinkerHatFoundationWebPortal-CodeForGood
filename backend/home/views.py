from contextlib import contextmanager
from urllib import response
from django.http import HttpResponse
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

from home.serializers import studentsSerializer, coursesSerializer, ClassSerializer,volunteerSerializer, question_answerSerializer, feedbackSerializer,testsSerializer,curriculumSerializer
from .forms import CreateUserForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import students,courses,Class,volunteer, question_answer, feedback, tests, curriculum

class StudentAPIView(APIView):
    def get (self, request):
        stud=students.objects.all()
        serializer_stud=studentsSerializer(stud, many=True)
        return Response(serializer_stud.data)
    def post(self, request):
        serializer_post = studentsSerializer(data=request.data)
        if serializer_post.is_valid():
            serializer_post.save()
            return Response(serializer_post.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer_post.errors, status=status.HTTP_400_BAD_REQUEST)            

class StudentDetails(APIView):
    def get_object(self, pk):
        # Returns an object instance that should 
        # be used for detail views.
        try:
            return students.objects.get(pk=pk)
        except students.DoesNotExist:
            return Response(studentsSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
    def get(self, request, pk):
        transformer = self.get_object(pk)
        serializer = studentsSerializer(transformer)
        return Response(serializer.data)
  
    def put(self, request, pk):
        transformer = self.get_object(pk)
        serializer = studentsSerializer(transformer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        transformer = self.get_object(pk)
        transformer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    

class CoursesAPIView(APIView):
    def get (self, request):
        stud=courses.objects.all()
        serializer_stud=coursesSerializer(stud, many=True)
        return Response(serializer_stud.data)
    def post(self, request):
        serializer_post = coursesSerializer(data=request.data)
        if serializer_post.is_valid():
            serializer_post.save()
            return Response(serializer_post.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer_post.errors, status=status.HTTP_400_BAD_REQUEST)            

class CoursesDetails(APIView):
    def get_object(self, pk):
        # Returns an object instance that should 
        # be used for detail views.
        try:
            return courses.objects.get(pk=pk)
        except courses.DoesNotExist:
            return Response(coursesSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
    def get(self, request, pk):
        transformer = self.get_object(pk)
        serializer = coursesSerializer(transformer)
        return Response(serializer.data)
  
    def put(self, request, pk):
        transformer = self.get_object(pk)
        serializer = coursesSerializer(transformer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        transformer = self.get_object(pk)
        transformer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    

class ClassAPIView(APIView):
    def get (self, request):
        stud=Class.objects.all()
        serializer_stud=ClassSerializer(stud, many=True)
        return Response(serializer_stud.data)
    def post(self, request):
        serializer_post = ClassSerializer(data=request.data)
        if serializer_post.is_valid():
            serializer_post.save()
            return Response(serializer_post.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer_post.errors, status=status.HTTP_400_BAD_REQUEST)            

class ClassDetails(APIView):
    def get_object(self, pk):
        # Returns an object instance that should 
        # be used for detail views.
        try:
            return Class.objects.get(pk=pk)
        except Class.DoesNotExist:
            return Response(ClassSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
    def get(self, request, pk):
        transformer = self.get_object(pk)
        serializer = ClassSerializer(transformer)
        return Response(serializer.data)
  
    def put(self, request, pk):
        transformer = self.get_object(pk)
        serializer = ClassSerializer(transformer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        transformer = self.get_object(pk)
        transformer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)            

class volunteerAPIView(APIView):
    def get (self, request):
        stud=volunteer.objects.all()
        serializer_stud=volunteerSerializer(stud, many=True)
        return Response(serializer_stud.data)
    def post(self, request):
        serializer_post = volunteerSerializer(data=request.data)
        if serializer_post.is_valid():
            serializer_post.save()
            return Response(serializer_post.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer_post.errors, status=status.HTTP_400_BAD_REQUEST)            

class volunteerDetails(APIView):
    def get_object(self, pk):
        # Returns an object instance that should 
        # be used for detail views.
        try:
            return volunteer.objects.get(pk=pk)
        except volunteer.DoesNotExist:
            return Response(volunteerSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
    def get(self, request, pk):
        transformer = self.get_object(pk)
        serializer = volunteerSerializer(transformer)
        return Response(serializer.data)
  
    def put(self, request, pk):
        transformer = self.get_object(pk)
        serializer = volunteerSerializer(transformer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        transformer = self.get_object(pk)
        transformer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    

class question_answerAPIView(APIView):
    def get (self, request):
        stud=question_answer.objects.all()
        serializer_stud=question_answerSerializer(stud, many=True)
        return Response(serializer_stud.data)
    def post(self, request):
        serializer_post = question_answerSerializer(data=request.data)
        if serializer_post.is_valid():
            serializer_post.save()
            return Response(serializer_post.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer_post.errors, status=status.HTTP_400_BAD_REQUEST)            

class question_answerDetails(APIView):
    def get_object(self, pk):
        try:
            return question_answer.objects.get(pk=pk)
        except question_answer.DoesNotExist:
            return Response(question_answerSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
    def get(self, request, pk):
        transformer = self.get_object(pk)
        serializer = question_answerSerializer(transformer)
        return Response(serializer.data)
  
    def put(self, request, pk):
        transformer = self.get_object(pk)
        serializer = question_answerSerializer(transformer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        transformer = self.get_object(pk)
        transformer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    

class feedbackAPIView(APIView):
    def get (self, request):
        stud=feedback.objects.all()
        serializer_stud=feedbackSerializer(stud, many=True)
        return Response(serializer_stud.data)
    def post(self, request):
        serializer_post = feedbackSerializer(data=request.data)
        if serializer_post.is_valid():
            serializer_post.save()
            return Response(serializer_post.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer_post.errors, status=status.HTTP_400_BAD_REQUEST)            

class feedbackDetails(APIView):
    def get_object(self, pk):
        # Returns an object instance that should 
        # be used for detail views.
        try:
            return feedback.objects.get(pk=pk)
        except feedback.DoesNotExist:
            return Response(feedbackSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
    def get(self, request, pk):
        transformer = self.get_object(pk)
        serializer = feedbackSerializer(transformer)
        return Response(serializer.data)
  
    def put(self, request, pk):
        transformer = self.get_object(pk)
        serializer = feedbackSerializer(transformer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        transformer = self.get_object(pk)
        transformer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    
# Create your views here.


class testsAPIView(APIView):
    def get (self, request):
        stud=tests.objects.all()
        serializer_stud=testsSerializer(stud, many=True)
        return Response(serializer_stud.data)
    def post(self, request):
        serializer_post = testsSerializer(data=request.data)
        if serializer_post.is_valid():
            serializer_post.save()
            return Response(serializer_post.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer_post.errors, status=status.HTTP_400_BAD_REQUEST)            

class testsDetails(APIView):
    def get_object(self, pk):
        # Returns an object instance that should 
        # be used for detail views.
        try:
            return tests.objects.get(pk=pk)
        except tests.DoesNotExist:
            return Response(testsSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
    def get(self, request, pk):
        transformer = self.get_object(pk)
        serializer = testsSerializer(transformer)
        return Response(serializer.data)
  
    def put(self, request, pk):
        transformer = self.get_object(pk)
        serializer = testsSerializer(transformer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        transformer = self.get_object(pk)
        transformer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    


class curriculumAPIView(APIView):
    def get (self, request):
        stud=curriculum.objects.all()
        serializer_stud=curriculumSerializer(stud, many=True)
        return Response(serializer_stud.data)
    def post(self, request):
        serializer_post = curriculumSerializer(data=request.data)
        if serializer_post.is_valid():
            serializer_post.save()
            return Response(serializer_post.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer_post.errors, status=status.HTTP_400_BAD_REQUEST)            

class curriculumDetails(APIView):
    def get_object(self, pk):
        # Returns an object instance that should 
        # be used for detail views.
        try:
            return curriculum.objects.get(pk=pk)
        except curriculum.DoesNotExist:
            return Response(curriculumSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
    def get(self, request, pk):
        transformer = self.get_object(pk)
        serializer = curriculumSerializer(transformer)
        return Response(serializer.data)
  
    def put(self, request, pk):
        transformer = self.get_object(pk)
        serializer = curriculumSerializer(transformer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        transformer = self.get_object(pk)
        transformer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    

def zoom(request):
    import jwt
    import requests
    import json
    from time import time


    # Enter your API key and your API secret
    API_KEY = 'jxddjzBJS86dKGygDfUU0Q'
    API_SEC = 'tGeUDSuXy7WjE72C7uENHQqKrMImdcuhl10O'

    # create a function to generate a token
    # using the pyjwt library


    def generateToken():
        token = jwt.encode(
            # Create a payload of the token containing
            # API Key & expiration time
            {'iss': API_KEY, 'exp': time() + 5000},

            # Secret used to generate token signature
            API_SEC,

            # Specify the hashing alg
            algorithm='HS256'
        )
        # print(token)
        return token


    # create json data for post requests
    meetingdetails = {"topic": "The title of your zoom meeting",
                    "type": 2,
                    "start_time": "2022-08-14T10: 21: 57",
                    "duration": "45",
                    "timezone": "Europe/Madrid",
                    "agenda": "test",

                    "recurrence": {"type": 1,
                                    "repeat_interval": 1
                                    },
                    "settings": {"host_video": "true",
                                "participant_video": "true",
                                "join_before_host": "False",
                                "mute_upon_entry": "False",
                                "watermark": "true",
                                "audio": "voip",
                                "auto_recording": "cloud"
                                }
                    }

    # send a request with headers including
    # a token and meeting details


    def createMeeting():
        headers = {'authorization': 'Bearer ' + generateToken(),
                'content-type': 'application/json'}
        r = requests.post(
            f'https://api.zoom.us/v2/users/me/meetings',
            headers=headers, data=json.dumps(meetingdetails))

        print("\n creating zoom meeting ... \n")
        # print(r.text)
        # converting the output into json and extracting the details
        y = json.loads(r.text)
        join_URL = y["join_url"]
        meetingPassword = y["password"]

        
        x=f'\n here is your zoom meeting link {join_URL} and your \
            password: "{meetingPassword}"\n'
        return HttpResponse(x)    


    # run the create meeting function
    createMeeting()
    # generateToken()          

def register(request):

    form=CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Account created for '+ user)
            return redirect('login')

    context={'form':form}
    return render(request,'register.html',context)
   
def loginPage(request):
    if request.method=='POST':
        username =request.POST.get('username')
        password =request.POST.get('password')

        user= authenticate(request, username=username, password=password)
        user= authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/about')
    return render(request,'loginPage.html')

def logoutUser(request):
    logout(request)
    return redirect('login')
   