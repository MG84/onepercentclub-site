from projects.models import (Project, IdeaPhase, PlanPhase, ActPhase, 
    ResultsPhase, BudgetLine, Message, Testimonial, BudgetCategory)
from django.contrib import admin

class IdeaPhaseInline(admin.StackedInline):
    model = IdeaPhase
    can_delete = False


class BudgetInline(admin.TabularInline):
    model = BudgetLine


class PlanPhaseInline(admin.StackedInline):
    model = PlanPhase


class ActPhaseInline(admin.StackedInline):
    model = ActPhase


class ResultsPhaseInline(admin.StackedInline):
    model = ResultsPhase


class ProjectAdmin(admin.ModelAdmin):
    inlines = [BudgetInline, IdeaPhaseInline, 
               PlanPhaseInline, ActPhaseInline, ResultsPhaseInline]


admin.site.register(Project, ProjectAdmin)
admin.site.register(Message)
admin.site.register(Testimonial)
admin.site.register(BudgetCategory)