from django.contrib.auth.forms import UserCreationForm # 新增
from django.shortcuts import render, redirect

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		print("Errors", form.errors)
		if form.is_valid():
			form.save()
			return redirect('/')
		else:
			return render(request, 'registration/register.html', {'form':form})
	else:
		form = UserCreationForm()
		context = {'form': form}
		return render(request, 'registration/register.html', context)

def index(request):
	if request.user.is_authenticated:
		username = request.user.username
	else:
		return redirect("/accounts/login")

	context = { "username": username}
	return render(request, "index.html", context)