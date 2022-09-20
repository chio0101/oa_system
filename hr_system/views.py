from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Employee
from .forms import EmployeeForm

# Create your views here.


@login_required(login_url="login")
def hr_clockin(request):
    login_name = request.user.username
    # employee = get_object_or_404(Employee, login_name=login_name)
    employee = ''
    context = {
        'employee': employee
    }
    return render(request, "hrs/hr_clockin.html", context)

@login_required(login_url="login")
def hr_info(request):
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
            return redirect('/')
        else:
            return render(request, "hrs/hr_info.html", {'form':form})
    else:
        form = EmployeeForm(initial=employee_dict)
        context = {'form': form}
        return render(request, "hrs/hr_info.html", context)