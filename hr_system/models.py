from django.db import models
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    email = models.CharField(max_length = 80)
    department = models.CharField(max_length = 80)
    username = models.ForeignKey(User, on_delete=models.CASCADE, to_field="username", db_column="username")

    def __str__(self):
        return self.first_name

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Employee._meta.fields]

    fields = ["first_name", "last_name", "email", "department", "username"] # 顯示欄位
    search_fields = ('first_name','last_name') # 搜尋欄位