from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import User
from .models import State
from .models import Comment

# Create your views here.

def index(request):
    prods = State.objects.all()
    return render(request, "templates_main/index.html", {"states": prods})

def about_state(request, states_id):
    prods = get_object_or_404(State, pk=states_id)
    return render(request, "templates_main/about_state.html", {"about_state": prods})

# def help(request):
#      prods = Groups.objects.all()
#      return render(request,"templates_student/student_groups.html",{"help": prods} )