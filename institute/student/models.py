from django.db import models


# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # profile_pic = models.ImageField(upload_to='profile_pic/StudentProfilePic/', null=True, blank=True)
    email = models.EmailField(unique=True)
    overall_progress = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    Admmission_date = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# class StudentProfile(models.Model):
#     student = models.OneToOneField(Student, on_delete=models.CASCADE)
#     profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
#
#     def __str__(self):
#         return f"Profile of {self.student.first_name} {self.student.last_name}"


class StudentAcedamicsRemarks(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    computer_science = models.CharField(max_length=300)
    mathematics = models.CharField(max_length=300)
    algorithms = models.CharField(max_length=300)
    database = models.CharField(max_length=300)

    def __str__(self):
        return f"Profile of {self.student.first_name} {self.student.last_name}"
