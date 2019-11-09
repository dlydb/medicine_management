# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from . import models

def select(request):
    if request.method == 'POST':
        
        redirect('detail_page.html')
        #return render(request, "detail_page.html")
    else:
        return render(request, "scheduler_page.html")

def schedule(request):
    print(models.Schedule.time_of_day)
    return render(request, "view_schedule.html")

def pilldetails(request):
    sch = request.POST
    
    if 'Pill 1' in sch:
        cmd = request.POST
        if 'time' in cmd:
            models.Medication.objects.create(name = cmd['pill_name'])
            models.Canister.objects.create(amount_remaining = 10,med_name = cmd['pill_name'])
            models.Schedule.objects.create(time_of_day = cmd['time'],amount = 1,canister_id=1)
    if 'Pill 2' in sch:
        cmd = request.POST
        if 'time' in cmd:
            models.Medication.objects.create(name = cmd['pill_name'])
            models.Canister.objects.create(amount_remaining = 10,med_name = cmd['pill_name'])
            models.Schedule.objects.create(time_of_day = cmd['time'],amount = 1,canister_id=2)
    if 'Pill 3' in sch:
        cmd = request.POST
        if 'time' in cmd:
            models.Medication.objects.create(name = cmd['pill_name'])
            models.Canister.objects.create(amount_remaining = 10,med_name = cmd['pill_name'])
            models.Schedule.objects.create(time_of_day = cmd['time'],amount = 1,canister_id=3)
    if 'Pill 4' in sch:
        cmd = request.POST
        if 'time' in cmd:
            models.Medication.objects.create(name = cmd['pill_name'])
            models.Canister.objects.create(amount_remaining = 10,med_name = cmd['pill_name'])
            models.Schedule.objects.create(time_of_day = cmd['time'],amount = 1,canister_id=4)
    if 'Pill 5' in sch:
        cmd = request.POST
        if 'time' in cmd:
            models.Medication.objects.create(name = cmd['pill_name'])
            models.Canister.objects.create(amount_remaining = 10,med_name = cmd['pill_name'])
            models.Schedule.objects.create(time_of_day = cmd['time'],amount = 1,canister_id=5)
    #print(models.Schedule.objects.get(id=1))
    #if 'time' in request.POST:
    #    print(request.POST['time'])
    #redirect('detail_page.html')
    return render(request, "detail_page.html")
