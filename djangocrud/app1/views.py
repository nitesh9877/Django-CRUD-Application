from django.shortcuts import render, redirect
from django.contrib import messages  # Import the messages framework
from .forms import EmpolyeeForm
from .models import Employee

# Create your views here.

# ======== Save Record ========== 
def Home(request):
    form = EmpolyeeForm()

    if request.method == 'POST':
        form = EmpolyeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record saved successfully!')  
            form = EmpolyeeForm()  # Clear form after saving

    data = Employee.objects.all()  # Get all data

    context = {
        'form': form,
        'data': data,
    }

    return render(request, 'app1/index.html', context)

# =========== Delete View=================
def Delete_record(request, id):
    a = Employee.objects.get(pk=id)
    a.delete()
    messages.success(request, 'Record deleted successfully!')  
    return redirect('/')

#============== Update View========================
def Update_Record(request, id):
    data = Employee.objects.get(pk=id)

    if request.method == "POST":
        form = EmpolyeeForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record updated successfully!')  
            return redirect('/')  # Redirect to home after update
    else:
        form = EmpolyeeForm(instance=data)

    context = {
        'form': form,
    }
    return render(request, 'app1/update.html', context)
