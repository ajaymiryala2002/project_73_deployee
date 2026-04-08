from django.shortcuts import render,redirect

from app.models import employee

from app.forms import emp_form


def new_employee(request):
    data = employee.objects.all()  # 
    form = emp_form()
    
    if request.method == 'POST':
        form = emp_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    
    context={
        'data':data,
        'form':form
    }   
    
    return render(request,'home.html',context)         


