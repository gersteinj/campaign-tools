from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Roster, Unit

# Create your views here.
def index(request):
    all_rosters = Roster.objects.all()
    # template = loader.get_template('rostertools/index.html')
    context = {'all_rosters': all_rosters}
    # return HttpResponse(template.render(context, request))
    return render(request, 'rostertools/index.html', context)

def view_roster(request, roster_id):
    roster = get_object_or_404(Roster, pk=roster_id)
    return render(request, 'rostertools/view-roster.html', {'roster': roster})

def create_roster(request):
    pass