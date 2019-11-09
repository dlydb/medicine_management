from django.urls import path
from . import views

urlpatterns = [
#    path('details/', views.pilldetails, name='details'),
#    path('select/', views.select, name='selectPill'),
    path('schedule/', views.schedule, name='schedule'),
    path('addNew/', views.create_reminder, name='addNew'),
]
