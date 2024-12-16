from django.db import models

class Course(models.Model):
    name  = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Lesson(models.Model):
    title = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    about = models.TextField()
    start = models.TimeField()
    end = models.TimeField()

    def __str__(self):
        return self.title


