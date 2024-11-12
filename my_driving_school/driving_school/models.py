from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import Group

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, null=True)
    phone_number = models.CharField(max_length=20, null=True)
    birth_date = models.DateField(null=True)
    hours_paid = models.IntegerField(default=0)
    lessons_taken = models.IntegerField(default=0)
    hours_available = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.username

class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Secretary(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

class Appointment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    hours = models.IntegerField(default=0)

    def __str__(self):
        return f"Rendez-vous avec {self.student.user.username} le {self.date} a {self.time}"

class StudentPackage(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    hours_available = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.student.user.username}'s Package"


@receiver(post_save, sender=User)
def assign_user_to_group(sender, instance, created, **kwargs):
    if created:
        if hasattr(instance, 'student'):
            group, created = Group.objects.get_or_create(name='Students')
            instance.groups.add(group)
        elif hasattr(instance, 'instructor'):
            group, created = Group.objects.get_or_create(name='Instructors')
            instance.groups.add(group)
        elif hasattr(instance, 'secretary'):
            group, created = Group.objects.get_or_create(name='Secretaries')
            instance.groups.add(group)
        elif hasattr(instance, 'admin'):
            group, created = Group.objects.get_or_create(name='Admins')
            instance.groups.add(group)