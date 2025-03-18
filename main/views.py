from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from datetime import datetime
from django.core.paginator import Paginator


from .models import State
from .models import Comment

# Create your views here.

def index(request):
    prods = State.objects.all()
    paginator = Paginator(prods, 5)
    page_number = request.GET.get('page')
    prods_on_page = paginator.get_page(page_number)
    return render(request, "templates_main/index.html", {"states": prods_on_page})


def about_state(request, states_id):
    prods = get_object_or_404(State, pk=states_id)
    comments_prods = Comment.objects.filter(state_id=states_id)
    return render(request, "templates_main/about_state.html", {"about_state": prods, "comments": comments_prods})

def comment_add(request, states_id):
    comment = Comment.objects.create(
        comment_text=request.POST['comment_text'],
        date_comment=datetime.now(),
        state_id_id=states_id
    )
    comment.save()
    return HttpResponseRedirect(reverse('main:states_detail', args=(states_id,)))

 