from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Employee
from .forms import EmployeeForm
from django.contrib import messages

# Create your views here.


@login_required(login_url="login")
def hr_clockin(request):
    username = request.user.username
    employee = Employee.objects.filter(username=username).values()
    if list(employee):
        employee_dict = list(employee)[0]
    # else:

    context = {
        'employee': employee
    }
    return render(request, "hrs/hr_clockin.html", context)

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