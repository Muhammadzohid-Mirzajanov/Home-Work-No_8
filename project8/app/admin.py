from django.contrib import admin
from .models import Course,Lesson

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id','name','description')
    search_fields = ('name',)

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'course', 'about', 'start', 'end')
    search_fields = ('title',)


