from django.db import models


class Student(models.Model):
    last_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    roll_no = models.CharField(max_length=20)
    email_id = models.EmailField(max_length=30)
    password=models.CharField(max_length=20)
    picture=models.CharField(max_length=120)

    def __str__(self):
        return self.roll_no

class Professor(models.Model):
    name = models.CharField(max_length=120)
    profession=models.CharField(max_length=120)
    roll_no=models.CharField(max_length=120)
    email_id=models.EmailField(max_length=120)
    description=models.CharField(max_length=500)
    picture=models.CharField(max_length=120)

    def __str__(self):
        return self.roll_no


class Message(models.Model):
    student_roll_no=models.ForeignKey(Student,on_delete=models.CASCADE)
    professor_roll_no=models.ForeignKey(Professor,on_delete=models.CASCADE)
    date=models.DateField()
    title=models.CharField(max_length=120)
    feed_back=models.CharField(max_length=500)

    def __str__(self):
        return self.title
