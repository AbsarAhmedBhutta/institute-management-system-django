from django.contrib import admin
from .models import Student,  StudentAcedamicsRemarks

# Register your models here.
# admin.site.register(Department)
# admin.AdminSite.register(StudentProfile)
admin.site.register(Student)
admin.site.register(StudentAcedamicsRemarks)
