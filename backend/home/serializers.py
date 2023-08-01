from rest_framework import serializers
from .models import students,courses,Class,volunteer, question_answer, feedback ,tests,curriculum

class studentsSerializer(serializers.ModelSerializer):
    class Meta:
        model=students
        fields = '__all__'

class coursesSerializer(serializers.ModelSerializer):
    class Meta:
        model=courses
        fields = '__all__'


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model=Class
        fields = '__all__'


class volunteerSerializer(serializers.ModelSerializer):
    class Meta:
        model=volunteer
        fields = '__all__'


class question_answerSerializer(serializers.ModelSerializer):
    class Meta:
        model=question_answer
        fields = '__all__'


class feedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model=feedback
        fields = '__all__'

class testsSerializer(serializers.ModelSerializer):
    class Meta:
        model=tests
        fields = '__all__'

class curriculumSerializer(serializers.ModelSerializer):
    class Meta:
        model=curriculum
        fields = '__all__'
