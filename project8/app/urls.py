from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('course/<int:course_id>/', views.lesson_list, name='lesson_list'),
    path('lesson/<int:lesson_id>/', views.lesson_detail, name='lesson_detail'),
    path('add-course/', views.add_course, name='add_course'),
    path('add-lesson/', views.add_lesson, name='add_lesson'),
    path('course/update/<int:course_id>/', views.update_course, name='update_course'),
    path('lesson/update/<int:lesson_id>/', views.update_lesson, name='update_lesson'),
]
