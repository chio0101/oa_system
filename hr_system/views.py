from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Employee, ClockInRecord
from .forms import EmployeeForm
from django.contrib import messages
from datetime import datetime
import pytz

# Create your views here.


@login_required(login_url="login")
def hr_clockin(request):
    timezone = pytz.timezone('Asia/Shanghai')
    current_datetime = datetime.now(timezone)
    current_date = current_datetime.date()
    current_time = current_datetime.time()
    current_date_str = current_datetime.strftime("%m/%d/%Y")
    current_time_str = current_datetime.strftime("%H:%M:%S")

    username = request.user.username
    employee = Employee.objects.filter(username=username).values()

    if list(employee):
        employee_dict = list(employee)[0]
        clock_in_msg = ''
        this_month_clock_in_record = ClockInRecord.objects.filter(
            date__year = current_date.year,
            date__month = current_date.month,
            username=User.objects.get(username=username)
        )

        if request.method == 'POST':
            today_clock_in_record, _ = ClockInRecord.objects.get_or_create(
                date=current_date, 
                username=User.objects.get(username=username)
            )
            clock_in_msg = "Successfully clock in, time: " + current_time_str

            if today_clock_in_record.clock_in(current_datetime):
                clock_in_msg = "Successfully clock in, time: " + current_time_str
            else:
                clock_in_msg = "Fail to clock in."
            today_clock_in_record.save()

        context = {
            'clock_in_record': this_month_clock_in_record,
            'employee': employee_dict,
            'clock_in_msg': clock_in_msg,
        }
        return render(request, "hrs/hr_clockin.html", context)
    else:
        messages.error(request, "Please fill in the profile first!")
        return redirect("hr:hr_profile")
        

@login_required(login_url="login")
def hr_profile(request):
    username = request.user.username
    employee = Employee.objects.filter(username=username).values()
    employee_dict = list(employee)[0] if list(employee) else {}

    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        print("Errors", form.errors)
        if form.is_valid():
            data = form.cleaned_data
            data['username'] = User.objects.get(username=username)
            employee = Employee.objects.update_or_create(username=username, defaults=data)

            messages.success(request, "Successfully edit profile!")
            return redirect('/hr')
        else:
            return render(request, "hrs/hr_profile.html", {'form':form})
    else:
        form = EmployeeForm(initial=employee_dict)
        context = {'form': form}
        return render(request, "hrs/hr_profile.html", context)