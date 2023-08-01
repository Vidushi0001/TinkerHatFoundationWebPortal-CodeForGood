from django.contrib import admin
from .models import students,courses,Class,volunteer, question_answer, feedback, tests,curriculum
# Register your models here.
admin.site.register(students)
admin.site.register(courses)
admin.site.register(Class)
admin.site.register(volunteer)
admin.site.register(question_answer)
admin.site.register(feedback)
admin.site.register(tests)
admin.site.register(curriculum)
