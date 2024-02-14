from django.contrib import admin
from .models import Employee
# Register your models here.


class AdminEmpoyee(admin.ModelAdmin):
    list_display = ['name', 'email', 'address', 'phone']


admin.site.register(Employee, AdminEmpoyee)
