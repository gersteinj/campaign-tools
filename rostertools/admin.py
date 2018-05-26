from django.contrib import admin
from .models import Roster, Unit

# Register your models here.

# admin.site.register(Roster)
# admin.site.register(Unit)

class UnitUnline(admin.StackedInline):
    model = Unit
    extra = 0

class RosterAdmin(admin.ModelAdmin):
    fields = ['owner', 'title']
    inlines = [UnitUnline]

admin.site.register(Roster, RosterAdmin)