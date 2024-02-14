from django.shortcuts import render, redirect
from .models import Employee

# Create your views here.


def Index(rqst):
    emp_data = Employee.objects.all()
    emp_data = {'emp_data': emp_data}
    return render(rqst, 'index.html', emp_data)


def add_employee(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        emp = Employee(name=name, email=email, address=address, phone=phone)
        emp.save()
        return redirect('home_page')
    return render(request, 'add_employee.html')


def edit_employee(request, id):
    try:
        if request.method == 'GET':
            emp = Employee.objects.get(id=id)
            context = {'emp': emp}
            return redirect(request, 'edit_employee.html', context)

    except Exception as e:
        print(f'Exception due to invaid operationv {e}')

    return render(request, 'edit_employee.html', context)


def edit_helper(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        emp = Employee.objects.get(id=id)
        emp.name = name
        emp.email = email
        emp.address = address
        emp.phone = phone
        emp.save()
        return redirect('home_page')

    return render(request, 'home.html')


def home(request):
    emp = Employee.objects.all()
    context = {'emp': emp}
    return render(request, 'home.html', context)


def delete_employee(request, id):
    emp = Employee.objects.get(id=id)
    emp.delete()
    return redirect('home_page')
