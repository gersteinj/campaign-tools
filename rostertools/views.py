from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.views import generic

from .models import Roster, Unit
from django.contrib.auth.models import User

# Create your views here.
class RosterListView(generic.ListView):
    model = Roster
    paginate_by = 10

class RosterDetailView(generic.DetailView):
    model = Roster

def view_roster(request, roster_id):
    roster = get_object_or_404(Roster, pk=roster_id)
    return render(request, 'rostertools/view-roster.html', {'roster': roster})

@login_required
def create_or_edit(request):
    return HttpResponse('create or edit rosters here')

@login_required
def user_rosters(request, username):
    owner = get_object_or_404(User, username=username)
    # return HttpResponse(f'{username}\'s rosters will appear here')
    # return HttpResponse(user.email)
    user_rosters = Roster.objects.filter(owner=owner)
    return render(request, 'rostertools/user-rosters.html', {'owner': owner, 'userrosters': user_rosters})
    # return HttpResponse(user_rosters)