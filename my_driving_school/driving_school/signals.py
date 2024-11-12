from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Student, StudentPackage

@receiver(post_save, sender=Student)
def create_student_package(sender, instance, created, **kwargs):
    if created:
        StudentPackage.objects.create(student=instance)
