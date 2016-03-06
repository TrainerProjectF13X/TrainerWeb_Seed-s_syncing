

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from .models import Post as Po
from django.contrib.auth.decorators import login_required
from UserLogin.models import RegularAccount as trainerDB
from UserLogin.models import RegularAccount as regularDB
from .forms import PostForm as Pf
from django.core.exceptions import ObjectDoesNotExist
@login_required
def post_list(request):
    current_user = request.user
    try:
        trainer_user = current_user.traineraccount
        queryset = regularDB.objects.filter(trainer=trainer_user.id)

    except ObjectDoesNotExist:
        return

    #queryset = Po.objects.all().order_by("-timestamp")

    context = {
        "objects_list": queryset,
        "title": "Lists"
    }

    return render(request, "posts/post_list.html", context)

@login_required
def post_detail(request, pk=None):
    instance = get_object_or_404(regularDB, id=pk)
    context = {
        "instance": instance,

    }
    return render(request, "posts/post_detail.html", context)

@login_required
def post_create(request):
    form = Pf(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Succesfully Created ")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "form": form,
        "iden": "create"
    }
    return render(request, "post_form.html", context)

@login_required
def post_update(request, pk=None):
    instance = get_object_or_404(Po, id=pk)
    form = Pf(request.POST or None, instance=instance)

    if form.is_valid():
        temp = form.save(commit=False)
        temp.save()
        messages.success(request, "Successfully updated ")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "iden": "update",
        "instance": instance,

        "form": form
    }

    return render(request, "post_form.html", context)


# Delete
@login_required
def post_delete(request, pk=None):
    instance = get_object_or_404(Po, id=pk)
    instance.delete()
    messages.success(request, "succesfully deleted")
    return redirect("posts:list")
    # return render()
