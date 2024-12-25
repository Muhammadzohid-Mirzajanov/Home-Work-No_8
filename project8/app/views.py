from django.shortcuts import render,get_list_or_404,redirect
from .models import Lesson,Course

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html',{'courses': courses})

def lesson_list(request,course_id):
    course = get_list_or_404(Course, id = course_id)
    lessons = course.lessons.all()
    return render(request,'lesson_list.html',{'lessons',lessons})

def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    return render(request, 'lesson_detail.html', {'lesson': lesson})

def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'add_course.html', {'form': form})

def add_lesson(request):
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = LessonForm()
    return render(request, 'add_lesson.html', {'form': form})