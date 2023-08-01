from django.db import models

class students(models.Model):
    student_name=models.CharField(max_length=100, blank=False, null=False)
    student_age=models.PositiveIntegerField()
    student_class=models.ForeignKey("Class", on_delete=models.CASCADE)
    student_city=models.CharField(max_length=100)
    def __str__(self):
        return self.student_name

class tests(models.Model):
    test_subject=models.TextField()
    test_marks=models.PositiveIntegerField()
    test_student=models.ForeignKey("students",on_delete=models.CASCADE)
    test_volunteer=models.ForeignKey("volunteer", on_delete=models.CASCADE)
    def __str__(self):
        return self.test_subject

class Class(models.Model):
    class_name=models.CharField(max_length=100, blank=False, null=False)
    class_strength=models.PositiveIntegerField()
    class_volunteer=models.ForeignKey("volunteer",on_delete=models.CASCADE)
    courses_assigned=models.ManyToManyField("courses")
    def __str__(self):
        return self.class_name    

class volunteer(models.Model):
    volunteer_name=models.CharField(max_length=100, blank=False, null=False)
    volunteer_duration=models.PositiveIntegerField()
    volunteer_Specialization=models.CharField(max_length=100)
    def __str__(self):
        return self.volunteer_name

class courses(models.Model):
    course_name=models.CharField(max_length=100, blank=False, null=False)
    course_class=models.PositiveIntegerField()
    course_videos_link=models.TextField(max_length=500) 
    course_instructor=models.ForeignKey("volunteer",on_delete=models.CASCADE)
    course_credits=models.IntegerField()
    def __str__(self):
        return self.course_name

class question_answer(models.Model):
    question=models.TextField()
    answer=models.TextField()
    user_asked=models.ForeignKey("students",on_delete=models.CASCADE, related_name="ask")
    user_answered=models.ManyToManyField("students" , related_name="answer")
    def __str__(self):
        return self.question

class feedback(models.Model):
    student=models.ForeignKey("students", on_delete=models.CASCADE)
    feedack_message=models.TextField()
    associated_volunteer=models.ForeignKey("volunteer", on_delete=models.CASCADE)
    def __str__(self):
        return self.feedack_message

class curriculum(models.Model):
    corresponding_cources=models.ForeignKey("courses",on_delete=models.CASCADE)
    curriculum_name=models.CharField(max_length=100)  
    curriculum_duration=models.IntegerField()
    Total_chapter=models.IntegerField()
    chapters_complete=models.IntegerField()
    def __str__(self):
        return self.curriculum_name


