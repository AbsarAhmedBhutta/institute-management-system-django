from django.db import models
from management.models import Department


# Create your models here.


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # profile_pic = models.ImageField(upload_to='profile_pic/TeacherProfilePic/', null=True, blank=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    hire_date = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

#
# class UserProfile(models.Model):
#     user = models.OneToOneField(Teacher, on_delete=models.CASCADE)
#     profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
#
#     def __str__(self):
#         return f"Profile of {self.user.first_name} {self.user.last_name}"
