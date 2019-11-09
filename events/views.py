from django.shortcuts import render, redirect
from .forms import PillFormset
from .models import Reminder

def create_reminder(request):
    template_name = 'add_reminder.html'
    heading_message = 'Add Reminder'
    if request.method=='GET':
        formset = PillFormset(request.GET or None)
    elif request.method=='POST':
        formset = PillFormset(request.POST)
        if formset.is_valid():
            for form in formset:
                name = form.cleaned_data.get('name')
                time = form.cleaned_data.get('time')
                if name and time:
                    Reminder(name=name,time=time).save()
            return redirect('schedule')
    return render(request, template_name, {
        'formset': formset,
        'heading': heading_message,
    })

def schedule(request):
    return render(request, 'schedule.html')
