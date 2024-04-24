from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from .models import User, Food, Project, Task, Sport, Routine, Event_project, Events
from django.shortcuts import render, get_object_or_404
from django.db.models import Max
import calendar
import matplotlib.pyplot as plt
import numpy as np
from schedule.models import Event
from datetime import datetime, date
from schedule.models.calendars import Calendar
from django.http import JsonResponse
import plotly.graph_objs as go
from persiantools.jdatetime import JalaliDate
 

def home(request):
    user = User.objects.get(username='rezas')
    routines = Routine.objects.filter(user_id = user.user_id)

    if request.method == 'POST':
        # Get the date value from the POST data
        date_value = request.POST.get('date_value')
        
        
        # Convert date string to datetime object
        chart_date = datetime.strptime(date_value, '%Y-%m-%d').date()

        # Get events for the selected date from the Event_project model
        events = Event_project.objects.filter(start_date=chart_date)

        # Create Plotly figure for the timeline chart
        fig = go.Figure()

        # Add traces for each event
        for event in events:
            fig.add_trace(go.Scatter(
                x=[event.start_datetime, event.end_datetime],
                y=[event.title, event.title],
                mode='lines+text',
                line=dict(color='#F97C35', width=15),  # Set all event lines to orange
                text=[event.title],  # Display event title within the line
                textposition='middle center',
                name=event.title
            ))

        # Customize layout
        fig.update_layout(
            plot_bgcolor='black',  # Set background color to black
            paper_bgcolor='#7A7B7C',  # Set border color to #7A7B7C
            font=dict(color='white'),  # Set text color to white
            # Remaining layout customization...
        )

        # Convert Plotly figure to HTML
        chart_div = fig.to_html(full_html=False)

        
        gregorian_date = datetime.strptime(date_value, '%Y-%m-%d').date()
        jalali_date = JalaliDate(gregorian_date).strftime("%Y-%m-%d")
        
        
        
        # Pass the HTML div containing the chart to the template
        context = {
            'name': user.name,
            'email': user.email,
            'events': events,
            'routines': routines, 
            'chart_div': chart_div,
            'jalali_date': jalali_date
        }
        
        return render(request, 'index.html', context)

    else:
        context = {
            'name': user.name,
            'email': user.email,
            'routines': routines
        }
        return render(request, 'index.html', context)




# code calendar ---------------------------------------------------------------------------------------------------------------------------


def index_open(request):  
    
    if request.method == 'POST':
        return redirect('index')
    
    return render(request,'index.html')


def index(request):  
    all_events = Events.objects.all()
    context = {
        "events":all_events,
    }
    return render(request,'index2.html',context)
 
def all_events(request):                                                                                                 
    all_events = Events.objects.all()                                                                                    
    out = []                                                                                                             
    for event in all_events:                                                                                             
        out.append({                                                                                                     
            'title': event.name,                                                                                         
            'id': event.id,                                                                                              
            'start': event.start.strftime("%m/%d/%Y, %H:%M:%S"),                                                         
            'end': event.end.strftime("%m/%d/%Y, %H:%M:%S"),                                                             
        })                                                                                                               
                                                                                                                      
    return JsonResponse(out, safe=False) 
 
def add_event(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    event = Events(name=str(title), start=start, end=end)
    event.save()
    data = {}
    return JsonResponse(data)
 
def update(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.start = start
    event.end = end
    event.name = title
    event.save()
    data = {}
    return JsonResponse(data)
 
def remove(request):
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.delete()
    data = {}
    return JsonResponse(data)