from django.db import models
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.urls import reverse
import datetime as dt

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

class ClockInRecord(models.Model):
    date = models.DateField(auto_now_add=True)
    morning_enter_time = models.TimeField(null=True)
    morning_leave_time = models.TimeField(null=True)
    afteroon_enter_time = models.TimeField(null=True)
    afteroon_leave_time = models.TimeField(null=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE, to_field="username", db_column="username")

    def clock_in(self, datetime):
        if dt.time(17,30,0) <= datetime.time():
            if self.afteroon_leave_time == None:
                self.afteroon_leave_time = datetime
                return True
            return False
        elif dt.time(13,30,0) <= datetime.time():
            if self.afteroon_enter_time == None:
                self.afteroon_enter_time = datetime
                return True
            return False
        elif dt.time(13,0,0) <= datetime.time():
            if self.morning_leave_time == None:
                self.morning_leave_time = datetime
                return True
            return False
        elif dt.time(8,30,0) <= datetime.time():
            if self.morning_enter_time == None:
                self.morning_enter_time = datetime
                return True
            return False


@admin.register(ClockInRecord)
class ClockInRecordAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ClockInRecord._meta.fields]

    fields = ["date", "morning_enter_time", "morning_leave_time", "afteroon_enter_time", "afteroon_leave_time", "username"] # 顯示欄位
    search_fields = ('date','username') # 搜尋欄位