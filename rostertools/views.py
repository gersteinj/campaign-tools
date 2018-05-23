from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Roster, Unit

# Create your views here.
def index(request):
    all_rosters = Roster.objects.all()
    template = loader.get_template('rostertools/index.html')
    context = {'all_rosters': all_rosters}
    return HttpResponse(template.render(context, request))

def view_roster(request, roster_id):
    roster = Roster.objects.get(pk=roster_id)
    template = loader.get_template('rostertools/view-roster.html')
    context={'roster': roster}
    return HttpResponse(template.render(context, request))
    