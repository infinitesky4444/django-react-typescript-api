from django.contrib import admin
from .models import Lesson, Question, Answer

# Register your models here.
admin.site.register(Lesson)
admin.site.register(Question)
admin.site.register(Answer)