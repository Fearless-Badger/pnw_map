from django.db import models

# Create your models here.

class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    abstract = models.CharField(max_length=2047)
    date = models.DateField()
    event_name = models.CharField(max_length=255)
    cost = models.IntegerField()
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=20)

    class Meta:
        db_table = 'events'

    def __str__(self):
        return str(self.event_name)


class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=255)
    mname = models.CharField(max_length=255, blank=True, null=True)
    lname = models.CharField(max_length=255)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=20)

    class Meta:
        db_table = 'students'

    def __str__(self):
        return f'{self.fname} {self.lname}'

class Registration(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)

    class Meta:
        unique_together = ('student', 'event')
        db_table = 'registration'

    def __str__(self):
        return f'{self.student} registered for {self.event}'
    