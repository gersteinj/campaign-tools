from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.auth.models import User

from .models import Roster, Unit
from .forms import RosterForm, UnitForm

# Create your views here.
class RosterListView(generic.ListView):
    model = Roster
    paginate_by = 10

class RosterDetailView(generic.DetailView):
    model = Roster

class UsersListView(generic.ListView):
    model = User

class UserRosterListView(generic.ListView):
    model = Roster

    def get(self, request, username):
        self.object_list = self.get_queryset()
        self.object_list = self.object_list.filter(owner__username=username)
    # queryset = Roster.objects.filter(owner__username='robotsinheels')
    # template_name = 'rostertools/user_rosters.html'
        return render(request, 'rostertools/user_rosters.html', {'object_list': self.object_list, 'owner': User.objects.get(username=username)})
        # return HttpResponse(self.object_list)

def add_roster(request):
    if request.method == 'POST':
        form = RosterForm(request.POST)
        if form.is_valid():
            roster = form.save(commit=False)
            roster.owner = request.user
            roster.save()
            return redirect('rostertools:view roster', pk=roster.pk)
    else:
        form = RosterForm()
    return render(request, 'rostertools/edit_roster.html', {'form': form})

def edit_roster(request, pk):
    roster = get_object_or_404(Roster, pk=pk)
    if request.method == 'POST':
        form = RosterForm(request.POST, instance=roster)
        if form.is_valid():
            roster = form.save(commit=False)
            roster.owner = request.user
            roster.save()
            return redirect('rostertools:view roster', pk=roster.pk)
    else:
        form = RosterForm(instance=roster)
    return render(request, 'rostertools/edit_roster.html', {'form': form})

def add_unit(request):
    if request.method == 'POST':
        form = UnitForm(request.POST)
        if form.is_valid():
            unit = form.save(commit=False)
            # roster.owner = request.user
            unit.save()
            return redirect('rostertools:index')
    else:
        form = UnitForm()
    return render(request, 'rostertools/edit_unit.html', {'form': form})

def edit_unit(request, pk):
    roster = get_object_or_404(Roster, pk=pk)
    if request.method == 'POST':
        form = UnitForm(request.POST, instance=roster)
        if form.is_valid():
            unit = form.save(commit=False)
            # roster.owner = request.user
            unit.save()
            return redirect('rostertools:index')
    else:
        form = UnitForm(instance=unit)
    return render(request, 'rostertools/edit_unit.html', {'form': form})


# @login_required
# def user_rosters(request, username):
#     owner = get_object_or_404(User, username=username)
#     # return HttpResponse(f'{username}\'s rosters will appear here')
#     # return HttpResponse(user.email)
#     user_rosters = Roster.objects.filter(owner=owner)
#     return render(request, 'rostertools/user-rosters.html', {'owner': owner, 'userrosters': user_rosters})
#     # return HttpResponse(user_rosters)

# def view_roster(request, roster_id):
#     roster = get_object_or_404(Roster, pk=roster_id)
#     return render(request, 'rostertools/view-roster.html', {'roster': roster})