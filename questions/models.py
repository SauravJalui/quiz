from django.db import models
import uuid

class Course(models.Model):
    id = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False)
    course_name = models.CharField(max_length=100)

    def __str__(self):
        return self.course_name

class Question(models.Model):
    '''This class has the questions with the course associated with it
    with 4 options of which last two are optional(in case of true/false questions)'''
    id = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    question = models.CharField(max_length=100)
    option_one = models.CharField(max_length=100)
    option_two = models.CharField(max_length=100)
    option_three = models.CharField(max_length=100, blank=True)
    option_four = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.question

class Answer(models.Model):
    '''This has the answer of the associated question'''
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    answer = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer